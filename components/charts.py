"""
Charts — Multi-bank FD return comparison using Altair.
Designed to match the Nivesh Mitra glassmorphic dark UI style.
"""

import pandas as pd
import altair as alt
import streamlit as st


def render_bank_comparison_chart(bank_results: list, duration_label: str):
    """
    Horizontal grouped bar chart: Principal vs Maturity Amount for each bank.
    Sorted by maturity amount (best first = top of chart).
    Displays inside a styled nm-chart-card wrapper.

    Args:
        bank_results:    Sorted list from calculate_all_banks() — best first.
        duration_label:  Human-readable tenure string (e.g. "1 Year").
    """
    if not bank_results:
        return

    rows = []
    for bank in bank_results:
        principal = bank["total"] - bank["returns"]   # original amount
        rows.append({"Bank": bank["name"], "Category": "Principal",       "Amount": principal})
        rows.append({"Bank": bank["name"], "Category": "Interest Earned", "Amount": bank["returns"]})

    df = pd.DataFrame(rows)

    # Order banks best-first (top of chart = index 0 = best)
    bank_order = [b["name"] for b in bank_results]

    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4)
        .encode(
            y=alt.Y(
                "Bank:N",
                sort=bank_order,
                axis=alt.Axis(
                    labelColor="#94A3B8",
                    labelFont="Plus Jakarta Sans",
                    labelFontSize=12,
                    tickColor="transparent",
                    domainColor="transparent",
                    title=None,
                    labelLimit=120,
                ),
            ),
            x=alt.X(
                "Amount:Q",
                stack="zero",
                axis=alt.Axis(
                    labelColor="#475569",
                    labelFont="JetBrains Mono",
                    labelFontSize=10,
                    gridColor="#1E2D45",
                    tickColor="transparent",
                    domainColor="transparent",
                    format=",.0f",
                    title=None,
                ),
            ),
            color=alt.Color(
                "Category:N",
                scale=alt.Scale(
                    domain=["Principal", "Interest Earned"],
                    range=["#3B82F6", "#10B981"],
                ),
                legend=alt.Legend(
                    orient="bottom",
                    labelColor="#94A3B8",
                    labelFont="Plus Jakarta Sans",
                    labelFontSize=12,
                    symbolSize=80,
                    titleColor="transparent",
                    padding=8,
                ),
            ),
            tooltip=[
                alt.Tooltip("Bank:N",     title="Bank"),
                alt.Tooltip("Category:N", title="Type"),
                alt.Tooltip("Amount:Q",   title="₹", format=",.0f"),
            ],
            order=alt.Order("Category:N", sort="ascending"),
        )
        .properties(
            height=max(200, len(bank_results) * 52),
            background="transparent",
            title=alt.Title(
                text=f"Maturity Comparison — {duration_label}",
                color="#475569",
                font="Plus Jakarta Sans",
                fontSize=11,
                fontWeight=700,
                anchor="start",
                offset=4,
            ),
        )
        .configure_view(strokeWidth=0)
        .configure_axis(grid=True)
    )

    st.markdown(
        '<div class="nm-chart-outer">'
        '<div class="nm-chart-card">',
        unsafe_allow_html=True,
    )
    st.altair_chart(chart, use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
