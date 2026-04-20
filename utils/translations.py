"""
utils/translations.py
Dictionary-based multilingual support for Nivesh Mitra AI.

Supported languages: English (en), Hindi (hi), Telugu (te)

Usage:
    from utils.translations import t
    message = t("welcome", lang="hi")
"""

TRANSLATIONS: dict = {

    # ── English ───────────────────────────────────────────────────────────────
    "en": {
        "welcome": (
            "Namaste! \U0001f64f I'm Nivesh Mitra — your personal FD advisor.\n\n"
            "Just tell me how much you want to invest and for how long.\n"
            "I'll instantly show you the best Fixed Deposit option!\n\n"
            "Examples:\n"
            "\u2022 \"1 lakh for 1 year\"\n"
            "\u2022 \"50,000 for 6 months\"\n"
            "\u2022 \"Best FD for 2 lakh\""
        ),
        "ask_amount": (
            "\U0001f4b0 How much would you like to invest?\n"
            "(e.g. 1 lakh,  50000,  \u20b92,00,000)"
        ),
        "ask_duration": (
            "\U0001f4c5 For how long would you like to invest?\n"
            "(e.g. 1 year,  6 months,  2 years)"
        ),
        "result_intro": "Here's what your {amount} grows into in {tenure} \U0001f447",
        "result_best":  "\U0001f3c6 {bank} gives the best return at {rate}% p.a.",
        "result_body":  "Your money becomes \u20b9{total} — you earn \u20b9{returns} extra!",
        "not_fd": (
            "I'm focused on helping you find the best Fixed Deposit. \U0001f60a\n\n"
            "Would you like to compare FD returns across top banks?\n"
            "Try: \"Best FD for 1 lakh\" or \"Compare rates for 1 year\""
        ),
        "offtopic": (
            "I'm sorry, I can only help with banking and Fixed Deposit information. \U0001f60a\n\n"
            "Would you like help comparing FD returns?"
        ),
        "followup_prompt": (
            "I'm here to help with Fixed Deposits! \U0001f60a\n\n"
            "You can ask:\n"
            "\u2022 \"Which bank is safest for FD?\"\n"
            "\u2022 \"What if I break my FD early?\"\n"
            "\u2022 \"Is FD better than RD?\""
        ),
        "booking_ready": (
            "\U0001f4cb Booking summary for {bank} is ready. "
            "Review below and open the bank portal when ready."
        ),
        "change_amount_saved": "Sure! Duration ({tenure}) is saved.\n\n\U0001f4b0 What's the new investment amount?",
        "change_duration_saved": "Got it! Amount ({amount}) is saved.\n\n\U0001f4c5 How long would you like to invest?",
        "new_calc_prompt": "Let's do another one! \U0001f504\n\n\U0001f4b0 How much would you like to invest this time?",
        "cta_label":      "\U0001f680 Proceed to Booking",
        "cta_sub":        "Secure your FD online in under 3 minutes — 100% paperless",
        "trust_rbi":      "RBI insured up to \u20b95 lakh",
        "trust_banks":    "Trusted banks only",
        "trust_charges":  "No hidden charges",
        "disclaimer":     "\u2139\ufe0f Rates are indicative and may vary across banks.",
        "tip_short":      "\U0001f4a1 Tip: A longer tenure (2\u20133 years) can increase your returns through compounding.",
        "safe_invest":    "\u2714 Safe investment option with predictable returns",
        "why_title":      "Why this bank?",
        "why_safe":       "\U0001f3e6 This bank is considered safe and reliable for fixed deposits.",
        "tenure_short":   "\U0001f4c5 Good for short-term parking of funds.",
        "tenure_long":    "\U0001f4c8 Better suited for long-term stable returns.",
        "pdf_download":   "\U0001f4c4 Download Summary PDF",
        "section_results": "\U0001f4c8 FD Calculation Results",
        "section_overview": "\U0001f4ca Bank Returns Overview",
        "section_compare": "\U0001f3e6 Top Banks Comparison",
        "edit_amount":    "\u270f\ufe0f Change Amount",
        "edit_duration":  "\U0001f4c5 Change Duration",
        "new_calc_btn":   "\U0001f504 New Calculation",
        "recording":      "\U0001f3a4 Recording\u2026 speak your query, then click Stop.",
        "mic_fail":       "Couldn't understand. Please type your query.",
    },

    # ── Hindi ─────────────────────────────────────────────────────────────────
    "hi": {
        "welcome": (
            "Namaste! \U0001f64f Main Nivesh Mitra hun — aapka personal FD advisor.\n\n"
            "Bas mujhe batayein kitna invest karna chahte hain aur kitne time ke liye.\n"
            "Main turant sabse accha Fixed Deposit option dikhaunga!\n\n"
            "Udaaharan:\n"
            "\u2022 \"1 lakh 1 saal ke liye\"\n"
            "\u2022 \"50,000 6 mahine ke liye\"\n"
            "\u2022 \"2 lakh ke liye best FD\""
        ),
        "ask_amount": (
            "\U0001f4b0 Aap kitna invest karna chahte hain?\n"
            "(jaise: 1 lakh,  50000,  \u20b92,00,000)"
        ),
        "ask_duration": (
            "\U0001f4c5 Kitne time ke liye invest karna chahte hain?\n"
            "(jaise: 1 saal,  6 mahine,  2 saal)"
        ),
        "result_intro": "Dekhen aapka {amount} {tenure} mein kitna banega \U0001f447",
        "result_best":  "\U0001f3c6 {bank} sabse zyada return deta hai \u2014 {rate}% p.a.",
        "result_body":  "Aapka paisa \u20b9{total} ho jayega \u2014 aap \u20b9{returns} extra kamayenge!",
        "not_fd": (
            "Main Fixed Deposits mein madad karta hun. \U0001f60a\n\n"
            "Kya aap FD returns compare karna chahte hain?\n"
            "Try karein: \"1 lakh ke liye best FD\""
        ),
        "offtopic": (
            "Maafi chahta hun, main sirf banking aur FD ki jankari de sakta hun. \U0001f60a\n\n"
            "Kya aap FD returns compare karna chahenge?"
        ),
        "followup_prompt": (
            "Main Fixed Deposits mein madad ke liye yahan hun! \U0001f60a\n\n"
            "Aap poochh sakte hain:\n"
            "\u2022 \"Sabse surakshit bank kaun sa hai?\"\n"
            "\u2022 \"FD tod ne par kya hoga?\"\n"
            "\u2022 \"FD ya RD kaun sa better hai?\""
        ),
        "booking_ready": (
            "\U0001f4cb {bank} ke liye booking summary tayyar hai. "
            "Neeche dekhein aur bank portal kholein."
        ),
        "change_amount_saved": "Theek hai! Avdhi ({tenure}) save ho gayi.\n\n\U0001f4b0 Nayi raashi kitni hogi?",
        "change_duration_saved": "Samajh gaya! Raashi ({amount}) save ho gayi.\n\n\U0001f4c5 Kitne time ke liye invest karna chahte hain?",
        "new_calc_prompt": "Ek aur calculate karein! \U0001f504\n\n\U0001f4b0 Is baar kitna invest karna chahte hain?",
        "cta_label":      "\U0001f680 Booking ke liye aagey badhein",
        "cta_sub":        "3 minute mein online FD secure karein — poori tarah paperless",
        "trust_rbi":      "RBI se \u20b95 lakh tak bima",
        "trust_banks":    "Sirf bharosemand bank",
        "trust_charges":  "Koi chhupa shulk nahi",
        "disclaimer":     "\u2139\ufe0f Dar sanketik hain aur bank se alag ho sakte hain.",
        "tip_short":      "\U0001f4a1 Sujhav: Lambi avdhi (2\u20133 saal) mein zyada returns milte hain.",
        "safe_invest":    "\u2714 Surakshit nivesh, nishchit returns ke sath",
        "why_title":      "Ye bank kyun?",
        "why_safe":       "\U0001f3e6 Yeh bank FD ke liye surakshit aur vishwasaniya maana jaata hai.",
        "tenure_short":   "\U0001f4c5 Chhote samay ke liye paisa rakhne ka accha vikalp.",
        "tenure_long":    "\U0001f4c8 Lambe samay ke liye sthir returns ke liye zyada upyukt.",
        "pdf_download":   "\U0001f4c4 Summary PDF Download Karein",
        "section_results": "\U0001f4c8 FD Ganana Parinam",
        "section_overview": "\U0001f4ca Bank Returns Overview",
        "section_compare": "\U0001f3e6 Top Banks Tulna",
        "edit_amount":    "\u270f\ufe0f Raashi Badlein",
        "edit_duration":  "\U0001f4c5 Avdhi Badlein",
        "new_calc_btn":   "\U0001f504 Nayi Ganana",
        "recording":      "\U0001f3a4 Recording ho rahi hai\u2026 bolein phir Stop dabayein.",
        "mic_fail":       "Samajh nahi aaya. Kripaya type karein.",
    },

    # ── Telugu ────────────────────────────────────────────────────────────────
    "te": {
        "welcome": (
            "Namaskaram! \U0001f64f Nenu Nivesh Mitra \u2014 mee personal FD advisor.\n\n"
            "Meeru entha invest cheyyalanukonnatho mariyu enta kalamu anukuntunnaro cheppandi.\n"
            "Vadam best Fixed Deposit option ventane chupistanu!\n\n"
            "Udaharanalu:\n"
            "\u2022 \"1 lakh 1 samvatsaram\"\n"
            "\u2022 \"50,000 6 masalaku\"\n"
            "\u2022 \"2 lakh ki best FD\""
        ),
        "ask_amount": (
            "\U0001f4b0 Meeru entha invest cheyyalanukunnaroo?\n"
            "(udaharanamu: 1 lakh,  50000,  \u20b92,00,000)"
        ),
        "ask_duration": (
            "\U0001f4c5 Enta kalamu invest cheyyalanukunnaroo?\n"
            "(udaharanamu: 1 samvatsaram,  6 masalu,  2 samvatsaraalu)"
        ),
        "result_intro": "Mee {amount} {tenure} lo enla penchutundho chudu \U0001f447",
        "result_best":  "\U0001f3c6 {bank} {rate}% p.a. tho adbutamaina return istundi.",
        "result_body":  "Mee dhanam \u20b9{total} avutundi \u2014 meeru \u20b9{returns} extra saampaadistaaru!",
        "not_fd": (
            "Nenu Fixed Deposits lo sahayam cheyyataanniki ikkade unnanu. \U0001f60a\n\n"
            "FD returns compare cheyyalanukunnaraa?\n"
            "Try cheyyandi: \"1 lakh ki best FD\""
        ),
        "offtopic": (
            "Xama cheyyandi, nenu banking mariyu FD samacharam mathrame cheppagalanu. \U0001f60a\n\n"
            "FD returns compare cheyyataanniki sahayam kavaalaa?"
        ),
        "followup_prompt": (
            "FD vishayaalo sahayam cheyyataanniki nenu ikkade unnanu! \U0001f60a\n\n"
            "Meeru adugavachu:\n"
            "\u2022 \"Anni bankuloo ethi surakshitam?\"\n"
            "\u2022 \"FD anukellipotey emi jarugatundi?\"\n"
            "\u2022 \"FD meluva RD aa?\""
        ),
        "booking_ready": (
            "\U0001f4cb {bank} booking summary ready ga undi. "
            "Kinda choodandi mariyu bank portal theravandi."
        ),
        "change_amount_saved": "Sare! Kalam ({tenure}) save chesamu.\n\n\U0001f4b0 Kotta amount entho cheppandi?",
        "change_duration_saved": "Ardham chesukunnanu! Amount ({amount}) save chesamu.\n\n\U0001f4c5 Enta kalamu invest cheyyalanukunnaroo?",
        "new_calc_prompt": "Maro calculation chesedamu! \U0001f504\n\n\U0001f4b0 Ee sari entha invest cheyyalanukunnaroo?",
        "cta_label":      "\U0001f680 Booking ki Munde Veyyandi",
        "cta_sub":        "3 nimishallo online FD secure cheyyandi \u2014 paperless",
        "trust_rbi":      "RBI \u20b95 lakh varaku bheema",
        "trust_banks":    "Nammakamaina bankulu mathrame",
        "trust_charges":  "Daagina charges levu",
        "disclaimer":     "\u2139\ufe0f Rakam chaalanidi, bankulu batti mariyu unnayi.",
        "tip_short":      "\U0001f4a1 Tip: Eedu kalam (2\u20133 samvatsaraalu) more returns istundi.",
        "safe_invest":    "\u2714 Nishchitha returns tho surakshitamaina investment",
        "why_title":      "Ee bank entuku?",
        "why_safe":       "\U0001f3e6 Ee bank FD ki surakshitamainatigi mariyu viswaasaniyamainatigi pariganistundi.",
        "tenure_short":   "\U0001f4c5 Takkuva kalamu dhanam pettataanniki manchidi.",
        "tenure_long":    "\U0001f4c8 Deergha kaala stable returns ki meluvu.",
        "pdf_download":   "\U0001f4c4 Summary PDF Download",
        "section_results": "\U0001f4c8 FD Calculation Results",
        "section_overview": "\U0001f4ca Bank Returns Overview",
        "section_compare": "\U0001f3e6 Top Banks Tulanam",
        "edit_amount":    "\u270f\ufe0f Amount Marchandi",
        "edit_duration":  "\U0001f4c5 Kalam Marchandi",
        "new_calc_btn":   "\U0001f504 Kotta Calculation",
        "recording":      "\U0001f3a4 Recording jarugatundi\u2026 cheppandi tarvata Stop click cheyyandi.",
        "mic_fail":       "Artham kaaledhu. Meeru type cheyyandi.",
    },
}

# Language code mapping from the dropdown display string
_LANG_MAP: dict[str, str] = {
    "English":  "en",
    "\u0939\u093f\u0902\u0926\u0940":    "hi",   # हिंदी
    "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41":   "te",   # తెలుగు
    # Other languages fall back to English for now
    "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd":    "en",   # தமிழ்
    "\u09ac\u09be\u0982\u09b2\u09be":    "en",   # বাংলা
    "\u092e\u0930\u093e\u0920\u0940":    "en",   # मराठी
    "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40":  "en",   # ਪੰਜਾਬੀ
}


def get_lang_code(display_name: str) -> str:
    """Map dropdown display string → language code (en/hi/te)."""
    return _LANG_MAP.get(display_name, "en")


def t(key: str, lang: str = "en", **kwargs) -> str:
    """
    Translate a string key to the requested language.

    Falls back to English if the key is missing in requested language.
    Supports format placeholders via kwargs.

    Args:
        key:    Translation key (e.g. "welcome", "ask_amount")
        lang:   Language code: "en", "hi", or "te"
        kwargs: Format arguments (e.g. amount="₹1 lakh")

    Example:
        t("result_intro", lang="hi", amount="₹1 lakh", tenure="1 Year")
    """
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    text = lang_dict.get(key, TRANSLATIONS["en"].get(key, key))
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass   # return unformatted string rather than crash
    return text
