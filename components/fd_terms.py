"""
components/fd_terms.py
FD Terms Explainer — shows 25 key FD terms in English, Hindi, or Telugu.

Usage:
    from components.fd_terms import render_fd_terms
    render_fd_terms(lang="hi")   # "en" | "hi" | "te"
"""

import streamlit as st

# ─────────────────────────────────────────────────────────────
#  TERM DATA  (exact content as specified — not generated)
# ─────────────────────────────────────────────────────────────

_TERMS: dict[str, list[dict]] = {

    "en": [
        {"t": "Fixed Deposit (FD)",      "d": "A safe investment where you deposit money for a fixed time and earn interest."},
        {"t": "Interest",                 "d": "The extra money you earn from the bank.", "e": "If you invest ₹1 lakh and get ₹7,000 extra, that ₹7,000 is interest."},
        {"t": "Interest Rate",            "d": "The percentage the bank gives you as return.", "e": "7% interest means ₹7,000 per year on ₹1 lakh."},
        {"t": "Principal",                "d": "The amount you originally invest.", "e": "If you deposit ₹1 lakh, that is your principal."},
        {"t": "Maturity Amount",          "d": "Total money you receive at the end (principal + interest).", "e": "₹1,00,000 → ₹1,07,000 after 1 year."},
        {"t": "Tenure",                   "d": "How long you keep your money invested.", "e": "1 year, 2 years, 5 years."},
        {"t": "Compound Interest",        "d": "Interest earned on both principal and past interest.", "e": "Your money grows faster over time."},
        {"t": "Simple Interest",          "d": "Interest calculated only on the original amount."},
        {"t": "Returns",                  "d": "The total profit you earn.", "e": "₹7,000 is your return."},
        {"t": "Premature Withdrawal",     "d": "Taking money out before the agreed time."},
        {"t": "Penalty",                  "d": "Charge applied if you break FD early."},
        {"t": "Senior Citizen Rate",      "d": "Extra interest for people above 60 years."},
        {"t": "Tax on FD",                "d": "Tax you pay on interest earned."},
        {"t": "TDS",                      "d": "Tax deducted by the bank before giving interest."},
        {"t": "Nominee",                  "d": "Person who receives your money if something happens to you."},
        {"t": "Auto Renewal",             "d": "FD automatically restarts after maturity."},
        {"t": "Cumulative FD",            "d": "Interest is paid at the end."},
        {"t": "Non-Cumulative FD",        "d": "Interest is paid monthly or quarterly."},
        {"t": "Safe Investment",          "d": "Low-risk way to grow money."},
        {"t": "Lock-in Period",           "d": "Time during which money cannot be withdrawn.", "e": "You cannot withdraw before 1 year."},
        {"t": "Liquidity",                "d": "How easily you can access your money."},
        {"t": "Deposit",                  "d": "Money you put in the bank."},
        {"t": "Withdrawal",               "d": "Taking money out of the bank."},
        {"t": "Short-Term FD",            "d": "FD for less than 1 year."},
        {"t": "Long-Term FD",             "d": "FD for more than 3 years."},
    ],

    "hi": [
        {"t": "फिक्स्ड डिपॉजिट (FD)",   "d": "एक सुरक्षित निवेश जिसमें आप निश्चित समय के लिए पैसा जमा करते हैं और ब्याज मिलता है।"},
        {"t": "ब्याज",                    "d": "बैंक द्वारा दिया गया अतिरिक्त पैसा।", "e": "₹1 लाख पर ₹7,000 मिलना ब्याज है।"},
        {"t": "ब्याज दर",                "d": "बैंक आपको कितने प्रतिशत रिटर्न देता है।", "e": "7% का मतलब ₹7,000 प्रति वर्ष।"},
        {"t": "मूलधन",                   "d": "आपने जो पैसा जमा किया है।", "e": "₹1 लाख आपका मूलधन है।"},
        {"t": "परिपक्व राशि",            "d": "अंत में मिलने वाला कुल पैसा।", "e": "₹1,00,000 → ₹1,07,000।"},
        {"t": "अवधि",                    "d": "पैसा कितने समय के लिए जमा रहता है।", "e": "1 साल, 2 साल।"},
        {"t": "चक्रवृद्धि ब्याज",       "d": "ब्याज पर भी ब्याज मिलना।"},
        {"t": "साधारण ब्याज",           "d": "केवल मूलधन पर मिलने वाला ब्याज।"},
        {"t": "रिटर्न",                  "d": "आपकी कुल कमाई।", "e": "₹7,000 रिटर्न है।"},
        {"t": "समय से पहले निकासी",     "d": "अवधि पूरी होने से पहले पैसा निकालना।"},
        {"t": "जुर्माना",                "d": "FD तोड़ने पर लगने वाला शुल्क।"},
        {"t": "वरिष्ठ नागरिक दर",       "d": "60 वर्ष से ऊपर वालों के लिए अधिक ब्याज।"},
        {"t": "कर (टैक्स)",              "d": "ब्याज पर लगने वाला टैक्स।"},
        {"t": "टीडीएस",                  "d": "बैंक द्वारा पहले से काटा गया टैक्स।"},
        {"t": "नामांकित व्यक्ति",        "d": "आपके बाद पैसा पाने वाला व्यक्ति।"},
        {"t": "स्वतः नवीनीकरण",         "d": "FD अपने आप फिर से शुरू होना।"},
        {"t": "संचयी FD",                "d": "ब्याज अंत में मिलता है।"},
        {"t": "गैर-संचयी FD",           "d": "ब्याज समय-समय पर मिलता है।"},
        {"t": "सुरक्षित निवेश",          "d": "कम जोखिम वाला निवेश।"},
        {"t": "लॉक-इन अवधि",            "d": "इस दौरान पैसा नहीं निकाल सकते।", "e": "1 साल तक पैसा बंद रहता है।"},
        {"t": "तरलता",                   "d": "पैसे तक जल्दी पहुंच।"},
        {"t": "जमा",                     "d": "बैंक में पैसा रखना।"},
        {"t": "निकासी",                  "d": "बैंक से पैसा निकालना।"},
        {"t": "अल्पकालीन FD",           "d": "कम समय की FD।"},
        {"t": "दीर्घकालीन FD",          "d": "लंबे समय की FD।"},
    ],

    "te": [
        {"t": "ఫిక్స్డ్ డిపాజిట్ (FD)", "d": "ఒక నిర్దిష్ట కాలానికి డబ్బు పెట్టి వడ్డీ పొందే సురక్షిత పెట్టుబడి."},
        {"t": "వడ్డీ",                   "d": "బ్యాంక్ మీ డబ్బుపై ఇచ్చే అదనపు మొత్తం.", "e": "₹1 లక్షపై ₹7,000 వడ్డీ."},
        {"t": "వడ్డీ రేటు",              "d": "బ్యాంక్ ఇచ్చే శాతం రాబడి.", "e": "7% అంటే ₹7,000."},
        {"t": "మూలధనం",                  "d": "మీరు పెట్టిన అసలు డబ్బు.", "e": "₹1 లక్ష."},
        {"t": "పరిపక్వ మొత్తం",          "d": "కాలం పూర్తయ్యాక వచ్చే మొత్తం.", "e": "₹1,00,000 → ₹1,07,000."},
        {"t": "కాల వ్యవధి",              "d": "డబ్బు ఎంతకాలం పెట్టుబడిగా ఉంటుంది.", "e": "1 సంవత్సరం."},
        {"t": "చక్రవడ్డీ",               "d": "వడ్డీపై కూడా వడ్డీ రావడం."},
        {"t": "సరళ వడ్డీ",               "d": "కేవలం మూలధనంపై వచ్చే వడ్డీ."},
        {"t": "రాబడి",                   "d": "పెట్టుబడిపై వచ్చే లాభం.", "e": "₹7,000."},
        {"t": "ముందస్తు ఉపసంహరణ",       "d": "కాలం పూర్తికాక ముందే డబ్బు తీసుకోవడం."},
        {"t": "జరిమానా",                 "d": "ముందుగా తీసుకుంటే పడే ఛార్జ్."},
        {"t": "సీనియర్ సిటిజన్ రేటు",   "d": "పెద్దవారికి ఎక్కువ వడ్డీ."},
        {"t": "పన్ను",                   "d": "వడ్డీపై చెల్లించాల్సిన పన్ను."},
        {"t": "TDS",                     "d": "బ్యాంక్ ముందుగానే తీసుకునే పన్ను."},
        {"t": "నామినీ",                  "d": "మీకు ఏదైనా జరిగితే డబ్బు పొందే వ్యక్తి."},
        {"t": "ఆటో రీన్యువల్",          "d": "FD మళ్లీ ఆటోమేటిక్గా ప్రారంభమవడం."},
        {"t": "క్యూములేటివ్ FD",         "d": "వడ్డీ చివర్లో ఇస్తారు."},
        {"t": "నాన్ క్యూములేటివ్ FD",   "d": "వడ్డీ తరచుగా ఇస్తారు."},
        {"t": "సురక్షిత పెట్టుబడి",     "d": "ప్రమాదం తక్కువగా ఉండే పెట్టుబడి."},
        {"t": "లాక్-ఇన్ పీరియడ్",      "d": "ఈ సమయంలో డబ్బు తీసుకోలేరు.", "e": "1 సంవత్సరం వరకు తీసుకోలేరు."},
        {"t": "లిక్విడిటీ",              "d": "డబ్బు సులభంగా పొందే అవకాశం."},
        {"t": "డిపాజిట్",               "d": "బ్యాంకులో డబ్బు వేయడం."},
        {"t": "ఉపసంహరణ",               "d": "డబ్బు తీసుకోవడం."},
        {"t": "తక్కువ కాల FD",          "d": "చిన్న కాలానికి FD."},
        {"t": "ఎక్కువ కాల FD",          "d": "పెద్ద కాలానికి FD."},
    ],
}

# Title strings per language
_TITLES = {
    "en": "\U0001f4d8 FD Terms Explained Simply",
    "hi": "\U0001f4d8 FD की शर्तें — सरल भाषा में",
    "te": "\U0001f4d8 FD నిబంధనలు — సులభంగా అర్థమయ్యేలా",
}

# Example label per language
_EG_LABEL = {
    "en": "Example:",
    "hi": "उदाहरण:",
    "te": "ఉదాహరణ:",
}


# ─────────────────────────────────────────────────────────────
#  RENDERER
# ─────────────────────────────────────────────────────────────

def render_fd_terms(lang: str = "en") -> None:
    """
    Render the FD Terms Explainer section.

    Args:
        lang: Language code — "en", "hi", or "te".
              Falls back to English for unsupported codes.
    """
    if lang not in _TERMS:
        lang = "en"

    terms   = _TERMS[lang]
    title   = _TITLES[lang]
    eg_lbl  = _EG_LABEL[lang]

    # ── Build inner HTML (flat — no blank lines) ──────────────────────────
    items_html = ""
    for i, term in enumerate(terms):
        divider = '<div style="height:1px;background:rgba(100,116,139,0.18);margin:10px 0;"></div>' if i > 0 else ""
        example = (
            f'<div style="font-size:11.5px;color:#64748b;margin-top:4px;font-style:italic;letter-spacing:0.01em;">'
            f'{eg_lbl} {term["e"]}'
            f'</div>'
        ) if "e" in term else ""
        items_html += (
            divider
            + f'<div style="padding:7px 0;">'
            + f'<div style="font-weight:700;font-size:15px;color:#e2e8f0;margin-bottom:4px;">{term["t"]}</div>'
            + f'<div style="font-size:13px;font-weight:400;color:#94a3b8;line-height:1.6;">{term["d"]}</div>'
            + example
            + '</div>'
        )

    # ── Outer card ────────────────────────────────────────────────────────
    # Uses inline styles only (no new CSS classes) to avoid any risk of
    # conflicting with chat_ui.py styles.
    st.markdown(
        '<div style="max-width:80%;margin:0 auto 32px;padding:0 28px;">'
        '<div style="'
        'background:rgba(13,20,38,0.70);'
        'border:1px solid rgba(99,102,241,0.25);'
        'border-radius:16px;'
        'padding:24px 28px;'
        'backdrop-filter:blur(18px);'
        'position:relative;'
        'overflow:hidden;'
        '">'
        # top accent line
        '<div style="'
        'position:absolute;top:0;left:0;right:0;height:2px;'
        'background:linear-gradient(90deg,#6366f1,#3b82f6);'
        'border-radius:16px 16px 0 0;'
        '"></div>'
        # section title
        f'<div style="font-size:13px;font-weight:800;text-transform:uppercase;'
        f'letter-spacing:0.12em;color:#818cf8;margin-bottom:18px;">{title}</div>'
        # scrollable terms list (max 380px so it doesn't dominate the page)
        '<div style="max-height:380px;overflow-y:auto;padding-right:8px;">'
        + items_html
        + '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )
