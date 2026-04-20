"""
Application constants for Nivesh Mitra AI.
"""

# ── Flow step identifiers ────────────────────────────────────────────────────
STEP_GREET        = "greet"
STEP_ASK_AMOUNT   = "ask_amount"
STEP_ASK_DURATION = "ask_duration"
STEP_RESULTS      = "results"
STEP_DONE         = "done"


# ── Bot prompt strings (plain text — no markdown, rendered safely in chat) ───

PROMPT_WELCOME = (
    "Namaste! \U0001f64f I'm Nivesh Mitra — your personal FD advisor.\n\n"
    "Just tell me how much you want to invest and for how long.\n"
    "I'll instantly show you the best Fixed Deposit option!\n\n"
    "Examples:\n"
    "\u2022 \"1 lakh for 1 year\"\n"
    "\u2022 \"50,000 for 6 months\"\n"
    "\u2022 \"Best FD for 2 lakh\""
)

PROMPT_ASK_AMOUNT = (
    "\U0001f4b0 How much would you like to invest?\n"
    "(e.g. 1 lakh, 50000, \u20b92,00,000)"
)

PROMPT_ASK_DURATION = (
    "\U0001f4c5 For how long would you like to invest?\n"
    "(e.g. 1 year, 6 months, 2 years)"
)

PROMPT_NOT_FD = (
    "I'm focused on helping you find the best Fixed Deposit. \U0001f60a\n\n"
    "Would you like to compare FD returns across top banks?\n"
    "Try: \"Best FD for 1 lakh\" or \"Compare rates for 1 year\""
)

PROMPT_OFFTOPIC = (
    "I'm sorry, I can only help with banking and Fixed Deposit information. \U0001f60a\n\n"
    "Would you like help comparing FD returns?"
)

PROMPT_TIP = (
    "\U0001f4a1 Tip: Investing for a longer tenure (2\u20133 years) can slightly "
    "increase your returns due to quarterly compounding."
)
