"""
Intent Engine — Detect FD intent and extract amount/duration from natural language.
"""
import re
from typing import Optional


# ── Universal text normaliser ────────────────────────────────────────────────
# Maps Hindi and Telugu number/time words to their English equivalents so that
# the downstream regex patterns work identically for all three languages.

_SCRIPT_MAP = [
    # ── Hindi ──────────────────────────────────────────────────────────────
    # amounts
    ("करोड़",        "crore"),
    ("करोड",        "crore"),
    ("लाख",         "lakh"),
    ("हजार",        "thousand"),
    # duration — order matters: longer strings first
    ("महीनों",      "months"),
    ("महीनें",     "months"),
    ("महीने",      "months"),
    ("महीना",      "month"),
    ("महीनो",      "months"),
    ("वर्षों",     "years"),
    ("वर्ष",       "year"),
    ("सालों",      "years"),
    ("साल",        "year"),
    # ── Telugu ─────────────────────────────────────────────────────────────
    # amounts
    ("కోటి",        "crore"),
    ("లక్షలు",      "lakhs"),
    ("లక్ష",        "lakh"),
    ("వేలు",        "thousand"),
    ("వేల",         "thousand"),
    # duration
    ("సంవత్సరాలు",  "years"),
    ("సంవత్సరం",   "year"),
    ("నెలలు",       "months"),
    ("నెల",         "month"),
    # ── Hinglish extras ────────────────────────────────────────────────────
    ("saal",        "year"),
    ("mahine",      "months"),
    ("mahina",      "month"),
    ("hajar",       "thousand"),
]

# Compile once at import time for performance
_SCRIPT_PATTERNS = [
    (re.compile(re.escape(src), re.IGNORECASE), dst)
    for src, dst in _SCRIPT_MAP
]


def normalize_text(text: str) -> str:
    """
    Transliterate Hindi / Telugu amount and duration tokens to English equivalents,
    strip ₹ symbol and Indian-style commas.

    Returns a clean, lowercase string ready for regex extraction.
    """
    result = text
    for pattern, replacement in _SCRIPT_PATTERNS:
        result = pattern.sub(replacement, result)
    # Strip ₹ and Indian-style commas
    result = result.replace("₹", " ").replace(",", " ")
    return result.lower()


# ── Keyword sets ─────────────────────────────────────────────────────────────

_FD_KEYWORDS = {
    "fd", "fixed deposit", "fixed-deposit", "invest", "investment",
    "best", "suggest", "compare", "return", "returns", "rate", "rates",
    "interest", "bank", "maturity", "deposit", "lakh", "crore", "rupee",
}

# Bank names trigger a flow reset when recognised mid-conversation
BANK_NAMES = {"sbi", "hdfc", "icici", "axis", "kotak", "rbi", "pnb", "bob"}

# New FD query keywords — detecting these mid-flow resets the calculation
NEW_QUERY_KEYWORDS = _FD_KEYWORDS | BANK_NAMES

_GREET_KEYWORDS = {"hi", "hello", "namaste", "hey", "start", "helo"}

# Topics that are clearly off-topic — only used at GREET step
_OFFTOPIC_KEYWORDS = {
    "weather", "news", "cricket", "sports", "movie", "recipe", "food",
    "music", "joke", "politics", "covid", "temperature", "today",
}


# ── Intent classification ────────────────────────────────────────────────────

def detect_intent(user_input: str) -> dict:
    """
    Classify the user's message intent.
    Returns dict with keys: intent ('high'|'medium'|'low'|'greet'|'offtopic'), score, tag.
    """
    text = user_input.lower()

    if any(kw in text for kw in ("best", "invest", "fd", "fixed deposit", "suggest", "compare")):
        return {"intent": "high",     "score": 0.9, "tag": "ready_to_invest"}

    if any(kw in text for kw in ("what is", "meaning", "explain", "tell me about", "how does")):
        return {"intent": "low",      "score": 0.4, "tag": "learning"}

    if any(kw in text for kw in _GREET_KEYWORDS):
        return {"intent": "greet",    "score": 0.5, "tag": "greeting"}

    if any(kw in text for kw in _OFFTOPIC_KEYWORDS):
        return {"intent": "offtopic", "score": 0.1, "tag": "off_topic"}

    return {"intent": "medium", "score": 0.6, "tag": "exploring"}


def is_fd_query(text: str) -> bool:
    """Return True if the message seems related to Fixed Deposits."""
    t = text.lower()
    return any(kw in t for kw in _FD_KEYWORDS)


def is_new_fd_query(text: str) -> bool:
    """
    Return True if the message looks like the start of a NEW FD calculation,
    even if a previous flow is still active.
    Triggers on: bank names, or core FD action keywords.
    """
    t = text.lower()
    has_bank   = any(b in t for b in BANK_NAMES)
    has_action = any(kw in t for kw in (
        "interest", "fd", "fixed deposit", "invest", "returns", "compare", "best"
    ))
    return has_bank or has_action


def is_offtopic(text: str) -> bool:
    """Return True if the message is clearly unrelated to banking / FDs."""
    t = text.lower()
    # Offtopic if it hits offtopic keywords AND has zero FD keywords
    hits_offtopic = any(kw in t for kw in _OFFTOPIC_KEYWORDS)
    hits_fd       = any(kw in t for kw in _FD_KEYWORDS | BANK_NAMES)
    return hits_offtopic and not hits_fd


# ── Amount extraction ────────────────────────────────────────────────────────

def extract_amount(text: str) -> Optional[float]:
    """
    Extract an investment amount (₹) from free text.

    Handles:
        "1 lakh", "2.5 lakhs", "1 crore", "₹50,000", "50k",
        "100000", "1,00,000", "50000", plain integers ≥ 1000.

    Returns float (rupees) or None.
    """
    # Normalise script (Hindi/Telugu→English) + strip ₹ and commas
    t = normalize_text(text)

    # "X crore(s)"
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:crores?|cr\.?)\b', t)
    if m:
        return float(m.group(1)) * 1_00_00_000

    # "X lakh(s)" / "X lac(s)"
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:lakhs?|lacs?|l)\b', t)
    if m:
        return float(m.group(1)) * 1_00_000

    # "X k" (thousands) — must not be followed by a letter to avoid false hits
    m = re.search(r'(\d+(?:\.\d+)?)\s*k\b', t)
    if m:
        return float(m.group(1)) * 1_000

    # Plain number ≥ 1000 (catches "100000", "50000")
    m = re.search(r'\b(\d{4,}(?:\.\d+)?)\b', t)
    if m:
        return float(m.group(1))

    # Plain 3-digit number ≥ 100 as a last resort when step = ask_amount
    # (handled in app.py by bypassing intent check at ask_amount step)
    m = re.search(r'\b(\d{3,}(?:\.\d+)?)\b', t)
    if m:
        return float(m.group(1))

    return None


# ── Duration extraction ──────────────────────────────────────────────────────

def extract_duration(text: str) -> Optional[float]:
    """
    Extract investment duration from free text. Returns years as float, or None.

    Handles:
        "1 year", "6 months", "2 yrs", "18 months", "1.5 year",
        "a year", "one year", "half year", "6 mahine",
        "1 साल", "6 महीने", "1 సంవత్సరం", "6 నెలలు"
    """
    # Normalise script (Hindi/Telugu→English keywords)
    t = normalize_text(text)

    # "half year" / "half a year"
    if re.search(r'\bhalf\s*(?:a\s*)?year\b', t):
        return 0.5

    # Months first (before years to avoid partial matches)
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:months?|mo\.?)\b', t)
    if m:
        return round(float(m.group(1)) / 12, 4)

    # Years / yrs / yr
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:years?|yrs?|yr)\b', t)
    if m:
        return float(m.group(1))

    # "a year" / "one year" / "ek saal"
    if re.search(r'\b(?:a|one|ek)\s+(?:year|saal)\b', t):
        return 1.0

    return None