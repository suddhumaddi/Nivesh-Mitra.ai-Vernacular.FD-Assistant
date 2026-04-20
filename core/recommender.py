"""
Recommender Engine — Select the best FD option and generate comparison insights.
"""


def recommend_best_bank(bank_results: list) -> dict:
    """
    Return the top-ranked bank from a calculate_all_banks() result list.
    The list is already sorted best-first, so index 0 is always the winner.

    Args:
        bank_results: Sorted list returned by calculate_all_banks()

    Returns:
        Dict with name, rate, returns, total, logo, tagline, booking_url.
    """
    if not bank_results:
        return {}
    return bank_results[0]


def get_tied_banks(bank_results: list) -> list:
    """
    Return banks with strictly identical returns to the top bank.

    Rules:
    - Uses STRICT equality on the rounded total (no tolerance band).
    - Returns at most 2 banks — never 3+ winners.
    - If only 1 bank qualifies, returns a single-item list (normal case).

    Args:
        bank_results: Sorted list from calculate_all_banks() — best first.

    Returns:
        List of 1 or 2 bank dicts.
    """
    if not bank_results:
        return []

    top_total = bank_results[0]["total"]

    # Strict equality — only banks whose rounded total matches exactly
    tied = [b for b in bank_results if b["total"] == top_total]

    # Cap at 2 winners maximum; sort ties alphabetically for determinism
    if len(tied) > 2:
        tied = sorted(tied[:2], key=lambda b: b["name"])

    return tied


def generate_earn_more_text(best: dict, runner_up: dict, all_results: list = None) -> str:
    """
    Generate a "Earn ₹X more than <bank>" callout for the winner card.

    Falls back to comparing with SBI when best and runner_up have identical
    returns — ensuring there is always a meaningful sentence.

    Args:
        best:        Best bank result dict
        runner_up:   Second-best bank result dict
        all_results: Full sorted list (optional) — used for SBI fallback

    Returns:
        Formatted string or empty string if truly no difference exists.
    """
    if not best or not runner_up:
        return ""

    diff = best["returns"] - runner_up["returns"]

    # If top two are tied (exact match), fall back to SBI comparison
    if diff == 0 and all_results and len(all_results) > 1:
        sbi = next((b for b in all_results if "sbi" in b["name"].lower()), None)
        fallback = sbi or all_results[-1]
        if fallback["name"] != best["name"]:
            diff = best["returns"] - fallback["returns"]
            if diff > 0:
                return f"Earn \u20b9{diff:,.0f} more than {fallback['name']}"
        return ""

    if diff <= 0:
        return ""
    return f"Earn \u20b9{diff:,.0f} more than {runner_up['name']}"


def generate_why_text(best: dict, all_results: list, duration_years: float) -> list:
    """
    Generate a 3-point "Why this bank?" explanation list.

    Args:
        best:           Best bank result dict
        all_results:    Full sorted list from calculate_all_banks()
        duration_years: Duration in years (float)

    Returns:
        List of plain-text reason strings (safe for chat bubbles).
    """
    reasons = []

    # 1. Highest rate among compared banks
    reasons.append(
        f"Highest rate: {best['name']} offers {best['rate']}% p.a. — "
        f"the best among all {len(all_results)} banks compared."
    )

    # 2. Extra earnings vs runner-up (index 1)
    if len(all_results) >= 2:
        runner_up = all_results[1]
        diff = best["returns"] - runner_up["returns"]
        if diff > 0:
            reasons.append(
                f"Extra earnings: You earn \u20b9{diff:,.0f} more than {runner_up['name']} "
                f"({runner_up['rate']}% p.a.) on the same investment."
            )

    # 3. Tenure suitability
    if duration_years <= 0.5:
        tenure_note = "Ideal for short-term parking — high liquidity with competitive returns."
    elif duration_years <= 1:
        tenure_note = "Perfect for a 1-year horizon — strong returns without long lock-in."
    elif duration_years <= 3:
        tenure_note = "Solid medium-term choice — balances safety and consistent growth."
    else:
        tenure_note = "Excellent for long-term wealth building — compounding works best here."
    reasons.append(f"Tenure fit: {tenure_note}")

    # 4. Competitive rate realism boost  (Part 5)
    reasons.append("Competitive rate compared to other leading banks.")

    return reasons


def recommend_fd(amount: float, duration: float, risk_level: str = "low") -> dict:
    """Legacy stub — kept for backward compatibility with old callers."""
    if duration <= 1:
        return {"bank": "AU Small Finance Bank", "rate": 8.2,
                "reason": "Short-term investment with good liquidity"}
    elif duration <= 3:
        return {"bank": "Suryoday Small Finance Bank", "rate": 8.5,
                "reason": "Balanced return and safety for medium duration"}
    else:
        return {"bank": "Ujjivan Small Finance Bank", "rate": 8.75,
                "reason": "Higher returns for long-term investment"}