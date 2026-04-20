"""
Nivesh Mitra AI — Main Application
Real guided FD investment flow with state machine.
"""

import json
import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
from pathlib import Path

from ai.llm import get_ai_response
from core.intent_engine import (
    detect_intent, extract_amount, extract_duration,
    is_fd_query, is_new_fd_query, is_offtopic,
)
from core.fd_calculator import calculate_all_banks
from core.recommender import (
    recommend_best_bank, generate_earn_more_text,
    generate_why_text, get_tied_banks,
)
from components.chat_ui import (
    inject_global_css,
    render_header,
    render_control_bar,
    render_chat_message,
    render_empty_state,
    render_fd_result_card,
    render_fd_comparison,
    render_cta_button,
    render_section_label,
    render_toast,
)
from components.charts import render_bank_comparison_chart
from components.voice import transcribe_audio
from components.fd_terms import render_fd_terms
from utils.translations import t, get_lang_code
from utils.pdf_generator import build_fd_pdf
from utils.constants import (
    STEP_GREET, STEP_ASK_AMOUNT, STEP_ASK_DURATION, STEP_RESULTS, STEP_DONE,
)

# ─────────────────────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Nivesh Mitra AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
#  BANK DATA  (cached — loaded once from JSON)
# ─────────────────────────────────────────────────────────────

@st.cache_data
def load_banks() -> list:
    path = Path(__file__).parent / "data" / "fd_data.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)["banks"]

BANKS = load_banks()

# ─────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────

_DEFAULTS: dict = {
    "messages":      [],
    "step":          STEP_GREET,
    "amount":        None,
    "duration":      None,
    "show_results":  False,
    "fd_results":    None,
    "best_bank":     None,
    "show_booking":  False,
    "voice_pending": False,
    "lang":          "en",            # active language code
    "user_data":     {"amount": None, "duration": None},
}

for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v


# ─────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────

def _now() -> str:
    return datetime.now().strftime("%I:%M %p")

def _bot(text: str):
    st.session_state.messages.append({"role": "bot", "content": text, "time": _now()})

def _user(text: str):
    st.session_state.messages.append({"role": "user", "content": text, "time": _now()})

def _lang() -> str:
    """Return the active language code."""
    return st.session_state.get("lang", "en")

def _t(key: str, **kwargs) -> str:
    """Translate a key using active session language."""
    return t(key, lang=_lang(), **kwargs)


def _tenure_label(years: float) -> str:
    if years < 1:
        months = int(round(years * 12))
        return f"{months} Month{'s' if months != 1 else ''}"
    if years == int(years):
        y = int(years)
        return f"{y} Year{'s' if y != 1 else ''}"
    return f"{years:.1f} Years"


def _amount_label(amount: float) -> str:
    if amount >= 1_00_000:
        lakhs = amount / 1_00_000
        if lakhs == int(lakhs):
            return f"\u20b9{int(lakhs)} lakh"
        return f"\u20b9{lakhs:.1f} lakh"
    return f"\u20b9{amount:,.0f}"


def _compute_results():
    amount   = st.session_state.amount
    duration = st.session_state.duration
    results  = calculate_all_banks(amount, duration, BANKS)
    best     = recommend_best_bank(results)
    st.session_state.fd_results   = results
    st.session_state.best_bank    = best
    st.session_state.show_results = True
    st.session_state.user_data    = {"amount": amount, "duration": duration}


def _reset_all():
    st.session_state.amount       = None
    st.session_state.duration     = None
    st.session_state.show_results = False
    st.session_state.fd_results   = None
    st.session_state.best_bank    = None
    st.session_state.show_booking = False
    st.session_state.step         = STEP_ASK_AMOUNT
    st.session_state.user_data    = {"amount": None, "duration": None}


def _reset_amount():
    st.session_state.amount       = None
    st.session_state.show_results = False
    st.session_state.fd_results   = None
    st.session_state.best_bank    = None
    st.session_state.show_booking = False
    st.session_state.step         = STEP_ASK_AMOUNT
    st.session_state.user_data["amount"] = None


def _reset_duration():
    st.session_state.duration     = None
    st.session_state.show_results = False
    st.session_state.fd_results   = None
    st.session_state.best_bank    = None
    st.session_state.show_booking = False
    st.session_state.step         = STEP_ASK_DURATION
    st.session_state.user_data["duration"] = None


def _comparison_dict(bank: dict, is_winner: bool,
                     runner_up: dict = None, all_results: list = None) -> dict:
    earn_more = ""
    if is_winner and runner_up:
        earn_more = generate_earn_more_text(bank, runner_up, all_results)
    return {
        "name":      bank["name"],
        "rate":      bank["rate"],
        "highlight": is_winner,
        "earn_more": earn_more,
        "stats": {
            "Maturity Amount": f"\u20b9{bank['total']:,.0f}",
            "Interest Earned": f"\u20b9{bank['returns']:,.0f}",
            "Tenure":          _tenure_label(st.session_state.duration),
        },
    }


# ─────────────────────────────────────────────────────────────
#  RENDERED PANELS
# ─────────────────────────────────────────────────────────────

def render_fd_bar_chart(principal: float, interest: float):
    data = pd.DataFrame({
        "Category": ["Principal", "Interest Earned"],
        "Amount":   [principal, interest],
        "Color":    ["#3B82F6", "#10B981"],
    })
    chart = (
        alt.Chart(data)
        .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
        .encode(
            x=alt.X("Category:N", axis=alt.Axis(
                labelColor="#94A3B8", labelFont="Plus Jakarta Sans", labelFontSize=13,
                tickColor="transparent", domainColor="#1E2D45", title=None,
            )),
            y=alt.Y("Amount:Q", axis=alt.Axis(
                labelColor="#94A3B8", labelFont="JetBrains Mono", labelFontSize=11,
                gridColor="#1E2D45", tickColor="transparent", domainColor="transparent",
                format=",.0f", title=None,
            )),
            color=alt.Color("Color:N", scale=None, legend=None),
            tooltip=[
                alt.Tooltip("Category:N"),
                alt.Tooltip("Amount:Q", format=",.2f", title="\u20b9"),
            ],
        )
        .properties(height=220, background="transparent")
        .configure_view(strokeWidth=0)
        .configure_axis(grid=True)
    )
    st.markdown('<div class="nm-chart-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="nm-chart-title">\U0001f4ca Return Breakdown</div>', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_why_bank_panel(best: dict, all_results: list, duration_years: float,
                           tied_banks: list = None):
    """'Why this bank?' panel with safety + tenure insights."""
    icons   = ["\U0001f3c6", "\U0001f4b0", "\U0001f4c5"]
    reasons = generate_why_text(best, all_results, duration_years)

    is_tie   = tied_banks and len(tied_banks) > 1
    tie_note = ""
    if is_tie:
        names    = " & ".join(b["name"] for b in tied_banks)
        tie_note = (
            f'<div class="nm-why-item">'
            f'<span class="nm-why-icon">\U0001f91d</span>'
            f'<span>Tie! {names} offer identical returns for this tenure. '
            f'All highlighted as best options.</span>'
            f'</div>'
        )

    # Dynamic tenure insight
    if duration_years <= 1:
        tenure_insight = _t("tenure_short")
    elif duration_years >= 3:
        tenure_insight = _t("tenure_long")
    else:
        tenure_insight = None

    items_html = tie_note + "".join(
        f'<div class="nm-why-item">'
        f'<span class="nm-why-icon">{icons[i % len(icons)]}</span>'
        f'<span>{reason}</span>'
        f'</div>'
        for i, reason in enumerate(reasons)
    )

    # Safety insight (always shown)
    items_html += (
        f'<div class="nm-why-item">'
        f'<span class="nm-why-icon">\U0001f3e6</span>'
        f'<span>{_t("why_safe")}</span>'
        f'</div>'
    )

    # Tenure-specific insight
    if tenure_insight:
        items_html += (
            f'<div class="nm-why-item">'
            f'<span class="nm-why-icon">\U0001f4c5</span>'
            f'<span>{tenure_insight}</span>'
            f'</div>'
        )

    title_icon = "\U0001f3c6\U0001f91d" if is_tie else "\U0001f9e0"
    st.markdown(
        '<div class="nm-why-outer">'
        '<div class="nm-why-card">'
        f'<div class="nm-why-title">{title_icon} {_t("why_title")}</div>'
        + items_html +
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_trust_indicators():
    """Trust badges + safe-investment line + disclaimer."""
    st.markdown(
        '<div class="nm-trust-row">'
        f'<div class="nm-trust-item green"><span class="nm-trust-icon">\U0001f6e1\ufe0f</span>{_t("trust_rbi")}</div>'
        f'<div class="nm-trust-item blue"><span class="nm-trust-icon">\u2714\ufe0f</span>{_t("trust_banks")}</div>'
        f'<div class="nm-trust-item amber"><span class="nm-trust-icon">\u2714\ufe0f</span>{_t("trust_charges")}</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    # Safe investment micro-trust
    st.markdown(
        f'<div class="nm-trust-row" style="margin-top:6px;">'
        f'<div class="nm-trust-item green">{_t("safe_invest")}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    # Disclaimer
    st.markdown(
        f'<div class="nm-trust-row" style="margin-top:4px;margin-bottom:4px;">'
        f'<div class="nm-trust-item" style="font-size:11px;color:#475569;">{_t("disclaimer")}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_edit_buttons():
    amount   = st.session_state.amount
    duration = st.session_state.duration
    t_label  = _tenure_label(duration) if duration else "—"
    amt_lbl  = _amount_label(amount) if amount else "—"

    st.markdown('<div class="nm-edit-bar">', unsafe_allow_html=True)
    col_a, col_d = st.columns(2)
    with col_a:
        if st.button(
            f"{_t('edit_amount')}  ({amt_lbl})",
            key="edit_amount_btn",
            use_container_width=True,
        ):
            _reset_amount()
            _bot(_t("change_amount_saved", tenure=t_label))
            st.rerun()
    with col_d:
        if st.button(
            f"{_t('edit_duration')}  ({t_label})",
            key="edit_duration_btn",
            use_container_width=True,
        ):
            _reset_duration()
            _bot(_t("change_duration_saved", amount=amt_lbl))
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def render_pdf_download(amount: float, duration: float, best: dict, all_results: list):
    """Download Summary PDF button."""
    pdf_bytes = build_fd_pdf(amount, duration, best, all_results)
    if pdf_bytes:
        st.download_button(
            label=_t("pdf_download"),
            data=pdf_bytes,
            file_name="fd_summary.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="pdf_download_btn",
        )


def render_booking_panel():
    best    = st.session_state.best_bank
    amount  = st.session_state.amount
    t_label = _tenure_label(st.session_state.duration)

    st.markdown(
        '<div class="nm-booking-outer">'
        '<div class="nm-booking-card">'
        '<div class="nm-booking-title">\U0001f4cb Booking Summary</div>'
        f'<div class="nm-booking-row"><span>Bank</span><strong>{best["name"]}</strong></div>'
        f'<div class="nm-booking-row"><span>Investment Amount</span><strong>\u20b9{amount:,.0f}</strong></div>'
        f'<div class="nm-booking-row"><span>Duration</span><strong>{t_label}</strong></div>'
        f'<div class="nm-booking-row"><span>Interest Rate</span><strong>{best["rate"]}% p.a.</strong></div>'
        f'<div class="nm-booking-row highlight"><span>Interest Earned</span><strong>\u20b9{best["returns"]:,.0f}</strong></div>'
        f'<div class="nm-booking-row highlight"><span>Maturity Amount</span><strong>\u20b9{best["total"]:,.0f}</strong></div>'
        f'<div class="nm-booking-note">\u26a0\ufe0f {_t("disclaimer")}</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    col_open, col_cancel = st.columns([3, 1])
    with col_open:
        try:
            st.link_button(
                f"\U0001f3e6 Open {best['name']} Portal \u2192",
                url=best["booking_url"],
                use_container_width=True,
                type="primary",
            )
        except (AttributeError, TypeError):
            st.markdown(f"**[\U0001f3e6 Open {best['name']} Portal \u2192]({best['booking_url']})**")
    with col_cancel:
        if st.button("\u2715 Cancel", key="cancel_booking", use_container_width=True):
            st.session_state.show_booking = False
            st.rerun()


# ─────────────────────────────────────────────────────────────
#  INPUT HANDLER — STATE MACHINE
# ─────────────────────────────────────────────────────────────

def handle_input(user_text: str):
    _user(user_text)

    step               = st.session_state.step
    extracted_amount   = extract_amount(user_text)
    extracted_duration = extract_duration(user_text)
    intent             = detect_intent(user_text)
    lang               = _lang()

    # ── NEW FD QUERY mid-flow / post-results → clean reset ───────────────────
    if step in (STEP_RESULTS, STEP_DONE, STEP_ASK_AMOUNT, STEP_ASK_DURATION):
        if is_new_fd_query(user_text):
            _reset_all()
            step = STEP_ASK_AMOUNT

    # ── Store extracted values (never overwrite existing) ─────────────────────
    if extracted_amount is not None and st.session_state.amount is None:
        st.session_state.amount = extracted_amount
    if extracted_duration is not None and st.session_state.duration is None:
        st.session_state.duration = extracted_duration

    # ── FAST PATH: both known ─────────────────────────────────────────────────
    if st.session_state.amount and st.session_state.duration:
        if not st.session_state.show_results:
            _compute_results()
            best    = st.session_state.best_bank
            t_label = _tenure_label(st.session_state.duration)
            a_label = _amount_label(st.session_state.amount)
            _bot(
                _t("result_intro", amount=a_label, tenure=t_label) + "\n\n"
                + _t("result_best", bank=best["name"], rate=best["rate"]) + "\n"
                + _t("result_body", total=f"{best['total']:,.0f}", returns=f"{best['returns']:,.0f}")
            )
            st.session_state.step = STEP_RESULTS
        else:
            _handle_followup(user_text, lang)
        return

    # ── Follow-up after results, no new data ──────────────────────────────────
    if st.session_state.show_results:
        _handle_followup(user_text, lang)
        return

    # ── DATA COLLECTION at ask_amount — bypass intent ─────────────────────────
    if step == STEP_ASK_AMOUNT:
        if st.session_state.amount is not None:
            _bot(_t("ask_duration"))
            st.session_state.step = STEP_ASK_DURATION
        else:
            _bot(_t("ask_amount"))
        return

    # ── DATA COLLECTION at ask_duration — bypass intent ───────────────────────
    if step == STEP_ASK_DURATION:
        _bot(_t("ask_duration"))
        return

    # ── GREET step: apply intent filtering ───────────────────────────────────
    if is_offtopic(user_text):
        _bot(_t("offtopic"))
        return

    has_fd_intent = (
        is_fd_query(user_text)
        or intent["intent"] in ("high", "medium")
        or (extracted_amount is not None or extracted_duration is not None)
    )

    if not has_fd_intent:
        _bot(_t("not_fd"))
        return

    # FD intent at greet → advance
    st.session_state.step = STEP_ASK_AMOUNT
    if st.session_state.amount is None:
        _bot(_t("ask_amount"))
    elif st.session_state.duration is None:
        _bot(_t("ask_duration"))
        st.session_state.step = STEP_ASK_DURATION


def _render_top3_cards(top3: list, is_tie: bool, tied_banks: list):
    """
    Render up to 3 bank comparison cards in a horizontal grid.

    Reuses the .nm-compare-card CSS already defined in chat_ui.py.
    We build the HTML manually here instead of calling render_fd_comparison
    (which only accepts exactly 2 cards) to support the 3-card layout.
    """
    if not top3:
        return

    def _card_html(bank: dict, idx: int) -> str:
        tied_set   = {b["name"] for b in (tied_banks or [])}
        is_winner  = (idx == 0) or (is_tie and bank["name"] in tied_set)
        card_cls   = "winner" if is_winner else "loser"
        rate_cls   = "green"  if is_winner else "blue"

        badge = '<div class="nm-best-badge">\U0001f3c6 Best Option</div>' if is_winner else ""
        if is_tie and is_winner:
            badge = '<div class="nm-best-badge">\U0001f3c6 Best Option (Tie)</div>'
        # Runner-Up badge for the second card (only when not a winner)
        if not is_winner and idx == 1:
            badge = (
                '<div class="nm-best-badge" style="background:rgba(148,163,184,0.15);'
                'border-color:rgba(148,163,184,0.3);color:#94a3b8;">'
                '\U0001f948 Runner-Up'
                '</div>'
            )

        # Earn-more line for the top card vs the first non-tied bank
        earn_html = ""
        if idx == 0 and len(top3) > 1:
            diff = bank["returns"] - top3[1]["returns"]
            if diff > 1:
                earn_html = (
                    f'<div class="nm-earn-more">'
                    f'\U0001f4a1 Earn \u20b9{diff:,.0f} more than {top3[1]["name"]}'
                    f'</div>'
                )

        stats_html = (
            f'<div class="nm-compare-stat"><span>Maturity Amount</span>'
            f'<span class="nm-compare-stat-val">\u20b9{bank["total"]:,.0f}</span></div>'
            f'<div class="nm-compare-stat"><span>Interest Earned</span>'
            f'<span class="nm-compare-stat-val">\u20b9{bank["returns"]:,.0f}</span></div>'
        )

        return (
            f'<div class="nm-compare-card {card_cls}">'
            + badge
            + f'<div class="nm-bank-name">{bank["name"]}</div>'
            + '<div class="nm-bank-sub">Fixed Deposit</div>'
            + f'<div class="nm-compare-rate {rate_cls}">{bank["rate"]}%</div>'
            + '<div class="nm-compare-rate-lbl">Annual Interest Rate</div>'
            + stats_html
            + earn_html
            + '</div>'
        )

    cards_html = "".join(_card_html(bank, i) for i, bank in enumerate(top3))
    st.markdown(
        '<div class="nm-compare-outer">'
        '<div class="nm-compare-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;">'
        + cards_html
        + '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def _handle_followup(user_text: str, _lang_unused: str = ""):
    if is_offtopic(user_text):
        _bot(_t("offtopic"))
        return
    if is_fd_query(user_text) or detect_intent(user_text)["intent"] == "high":
        ai_reply = get_ai_response(user_text, _lang())
        _bot(ai_reply)
    else:
        _bot(_t("followup_prompt"))


# ─────────────────────────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────────────────────────

def main():
    # 1. CSS
    inject_global_css()

    # 2. Header
    _step_num = {
        STEP_GREET: 1, STEP_ASK_AMOUNT: 1, STEP_ASK_DURATION: 1,
        STEP_RESULTS: 2, STEP_DONE: 3,
    }
    render_header(current_step=_step_num.get(st.session_state.step, 1))

    # 3. Control bar — capture language selection and sync to session state
    lang_display, _ = render_control_bar()
    lang_code = get_lang_code(lang_display)
    if st.session_state.lang != lang_code:
        st.session_state.lang = lang_code

    # 3b. FD Terms Explainer (below control bar, above chat)
    render_fd_terms(lang=lang_code)

    # 4. Auto-greet on first load
    if not st.session_state.messages:
        _bot(_t("welcome"))

    # 5. Chat history
    st.markdown('<div class="nm-chat-wrapper">', unsafe_allow_html=True)
    if not st.session_state.messages:
        render_empty_state()
    else:
        for msg in st.session_state.messages:
            render_chat_message(
                role=msg["role"],
                content=msg["content"],
                timestamp=msg.get("time", ""),
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # 6. Results — rendered OUTSIDE chat
    if st.session_state.show_results and st.session_state.fd_results:
        results    = st.session_state.fd_results
        # ── Deduplicate by bank name (safety net for any duplicate entries) ──
        _seen = set()
        results = [
            b for b in results
            if b["name"] not in _seen and not _seen.add(b["name"])
        ]
        best       = st.session_state.best_bank
        amount     = st.session_state.amount
        dur        = st.session_state.duration
        t_label    = _tenure_label(dur)
        tied_banks = get_tied_banks(results)
        is_tie     = len(tied_banks) > 1

        # ── Edit buttons ──
        render_edit_buttons()

        # ── FD Result Card ──
        render_section_label(_t("section_results"))
        render_fd_result_card(
            principal=amount,
            interest_earned=best["returns"],
            total_amount=best["total"],
            tenure=t_label,
            rate=best["rate"],
        )

        # ── Why this bank ──
        render_why_bank_panel(best, results, dur, tied_banks=tied_banks)

        # ── Multi-bank comparison chart (all banks) ──
        render_section_label(_t("section_overview"))
        render_bank_comparison_chart(results, t_label)

        # ── Principal vs Interest bar chart ──
        render_fd_bar_chart(amount, best["returns"])

        # ── Top 3 banks comparison cards ──
        render_section_label(_t("section_compare"))
        _render_top3_cards(results[:3], is_tie, tied_banks)

        # ── Tip (short tenure) ──
        if dur <= 1:
            st.markdown(
                f'<div class="nm-trust-row" style="margin-top:4px;margin-bottom:20px;">'
                f'<div class="nm-trust-item blue" style="font-size:13px;">{_t("tip_short")}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

        # ── PDF Download ──
        _, col_pdf, _ = st.columns([3, 2, 3])
        with col_pdf:
            render_pdf_download(amount, dur, best, results)

        # ── CTA or Booking Panel ──
        if st.session_state.show_booking:
            render_booking_panel()
        else:
            cta_clicked = render_cta_button(
                label=_t("cta_label"),
                sub=_t("cta_sub"),
            )
            render_trust_indicators()

            if cta_clicked:
                st.session_state.show_booking = True
                st.session_state.step = STEP_DONE
                _bot(_t("booking_ready", bank=best["name"]))
                st.rerun()

        # ── New Calculation ──
        _, col_reset, _ = st.columns([3, 2, 3])
        with col_reset:
            if st.button(_t("new_calc_btn"), key="reset_btn", use_container_width=True):
                _reset_all()
                _bot(_t("new_calc_prompt"))
                st.rerun()

    # 7. Input area
    st.markdown('<div class="nm-input-wrapper"><div class="nm-input-inner">', unsafe_allow_html=True)
    col_input, col_send, col_mic = st.columns([8, 1, 1])

    with col_input:
        user_input = st.text_input(
            label="message",
            placeholder="Ask about FD rates, returns, bank comparison\u2026",
            label_visibility="collapsed",
            key="chat_input",
        )
    with col_send:
        send = st.button("Send \u2192", key="send_btn", use_container_width=True)
    with col_mic:
        mic_open = st.button("\U0001f3a4", key="voice_btn", use_container_width=True,
                             help="Click to record voice input")
    st.markdown('</div></div>', unsafe_allow_html=True)

    # 8. Voice widget
    if mic_open:
        st.session_state.voice_pending = True

    if st.session_state.voice_pending:
        st.markdown(
            f'<div class="nm-voice-processing">{_t("recording")}</div>',
            unsafe_allow_html=True,
        )
        audio_value = st.audio_input(
            label="Voice Input",
            label_visibility="collapsed",
            key="voice_recorder",
        )
        if audio_value is not None:
            transcript = transcribe_audio(audio_value.getvalue())
            st.session_state.voice_pending = False
            if transcript:
                render_toast(f"\U0001f3a4 Heard: \"{transcript}\"")
                handle_input(transcript)
                st.rerun()
            else:
                render_toast(_t("mic_fail"))
                st.rerun()

    # 9. Text submission
    if send and user_input.strip():
        handle_input(user_input.strip())
        st.rerun()


if __name__ == "__main__":
    main()