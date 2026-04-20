"""
PDF generator for Nivesh Mitra AI FD Summary.
Uses reportlab (already in the project's environment).

Usage:
    from utils.pdf_generator import build_fd_pdf
    pdf_bytes = build_fd_pdf(amount, duration, best_bank, all_results)
    st.download_button("Download", pdf_bytes, "fd_summary.pdf", "application/pdf")
"""

import io
from datetime import datetime


def build_fd_pdf(
    amount: float,
    duration_years: float,
    best: dict,
    all_results: list,
) -> bytes:
    """
    Build a clean FD summary PDF and return it as bytes.

    Args:
        amount:         Principal invested (₹)
        duration_years: Duration in years
        best:           Best bank result dict
        all_results:    Full sorted list from calculate_all_banks()

    Returns:
        PDF content as raw bytes — pass directly to st.download_button.
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import cm
        from reportlab.lib import colors
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
        )
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
    except ImportError:
        return b""   # graceful no-op if reportlab somehow missing

    buffer = io.BytesIO()
    margin = 2 * cm

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin,  bottomMargin=margin,
        title="FD Investment Summary — Nivesh Mitra AI",
        author="Nivesh Mitra AI",
    )

    styles = getSampleStyleSheet()

    # ── Custom styles ─────────────────────────────────────────────────────────
    DARK          = colors.HexColor("#0F172A")
    GREEN         = colors.HexColor("#10B981")
    BLUE          = colors.HexColor("#3B82F6")
    MUTED         = colors.HexColor("#64748B")
    LIGHT_BG      = colors.HexColor("#F1F5F9")
    WINNER_BG     = colors.HexColor("#ECFDF5")

    h1 = ParagraphStyle("h1", parent=styles["Heading1"],
                         fontSize=22, textColor=DARK, spaceAfter=4, alignment=TA_CENTER,
                         fontName="Helvetica-Bold")
    h2 = ParagraphStyle("h2", parent=styles["Heading2"],
                         fontSize=13, textColor=BLUE, spaceBefore=14, spaceAfter=6,
                         fontName="Helvetica-Bold")
    body = ParagraphStyle("body", parent=styles["Normal"],
                           fontSize=10, textColor=DARK, leading=15)
    muted = ParagraphStyle("muted", parent=styles["Normal"],
                            fontSize=9, textColor=MUTED, leading=13)
    center = ParagraphStyle("center", parent=styles["Normal"],
                             fontSize=9, textColor=MUTED, alignment=TA_CENTER)

    # ── Tenure label helper ───────────────────────────────────────────────────
    def _tenure(years):
        if years < 1:
            m = int(round(years * 12))
            return f"{m} Month{'s' if m != 1 else ''}"
        if years == int(years):
            y = int(years)
            return f"{y} Year{'s' if y != 1 else ''}"
        return f"{years:.1f} Years"

    def _fmt(n):
        return f"\u20b9{n:,.0f}"

    tenure_label = _tenure(duration_years)
    today        = datetime.now().strftime("%d %B %Y, %I:%M %p")

    story = []

    # ── Header ────────────────────────────────────────────────────────────────
    story.append(Paragraph("\U0001f4b0 Nivesh Mitra AI", h1))
    story.append(Paragraph("Fixed Deposit Investment Summary", center))
    story.append(Spacer(1, 0.3 * cm))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
    story.append(Spacer(1, 0.4 * cm))

    # ── Investment details ────────────────────────────────────────────────────
    story.append(Paragraph("Your Investment", h2))
    details_data = [
        ["Principal",      _fmt(amount)],
        ["Duration",       tenure_label],
        ["Generated on",   today],
    ]
    details_table = Table(details_data, colWidths=["40%", "60%"])
    details_table.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (0, -1), LIGHT_BG),
        ("FONTNAME",    (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE",    (0, 0), (-1, -1), 10),
        ("TEXTCOLOR",   (0, 0), (-1, -1), DARK),
        ("FONTNAME",    (0, 0), (0, -1), "Helvetica-Bold"),
        ("TOPPADDING",  (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("GRID",        (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, LIGHT_BG]),
    ]))
    story.append(details_table)
    story.append(Spacer(1, 0.5 * cm))

    # ── Best option ───────────────────────────────────────────────────────────
    story.append(Paragraph("\U0001f3c6 Best Option", h2))
    winner_data = [
        ["Bank",             best["name"]],
        ["Interest Rate",    f"{best['rate']}% p.a."],
        ["Interest Earned",  _fmt(best["returns"])],
        ["Maturity Amount",  _fmt(best["total"])],
    ]
    winner_table = Table(winner_data, colWidths=["40%", "60%"])
    winner_table.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), WINNER_BG),
        ("FONTNAME",    (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",    (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE",    (0, 0), (-1, -1), 10),
        ("TEXTCOLOR",   (0, 0), (-1, -1), DARK),
        ("TEXTCOLOR",   (1, -2), (1, -1), GREEN),
        ("FONTNAME",    (1, -2), (1, -1), "Helvetica-Bold"),
        ("TOPPADDING",  (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("GRID",        (0, 0), (-1, -1), 0.5, GREEN),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WINNER_BG, colors.white]),
    ]))
    story.append(winner_table)
    story.append(Spacer(1, 0.5 * cm))

    # ── All-bank comparison table ─────────────────────────────────────────────
    story.append(Paragraph("Bank Comparison", h2))
    header = ["Bank", "Rate (% p.a.)", "Interest Earned", "Maturity Amount"]
    rows   = [header]
    for i, bank in enumerate(all_results[:5]):   # show top 5 at most
        rows.append([
            bank["name"],
            f"{bank['rate']}%",
            _fmt(bank["returns"]),
            _fmt(bank["total"]),
        ])

    comp_table = Table(rows, colWidths=["30%", "18%", "26%", "26%"])
    comp_style = [
        ("BACKGROUND",    (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("TEXTCOLOR",     (0, 1), (-1, -1), DARK),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BG]),
        # Highlight winner row
        ("BACKGROUND",    (0, 1), (-1, 1), WINNER_BG),
        ("TEXTCOLOR",     (1, 1), (-1, 1), GREEN),
        ("FONTNAME",      (0, 1), (-1, 1), "Helvetica-Bold"),
    ]
    comp_table.setStyle(TableStyle(comp_style))
    story.append(comp_table)
    story.append(Spacer(1, 0.6 * cm))

    # ── Disclaimer ────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=0.5, color=MUTED))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Disclaimer: Rates are indicative and may vary across banks. "
        "This summary is generated by Nivesh Mitra AI for informational purposes only. "
        "Please verify rates at the bank's official portal before investing.",
        muted,
    ))

    # ── Build ─────────────────────────────────────────────────────────────────
    doc.build(story)
    return buffer.getvalue()
