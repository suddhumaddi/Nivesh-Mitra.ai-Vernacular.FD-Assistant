"""
FD Calculator — Quarterly Compound Interest

Formula: A = P × (1 + r/400)^(4t)
  P = principal (₹)
  r = annual rate (%)
  t = time (years)
"""


def calculate_fd(principal: float, rate: float, time: float) -> dict:
    """
    Compute FD maturity using quarterly compounding.

    Args:
        principal: Amount invested (₹)
        rate:      Annual interest rate (%)
        time:      Duration in years

    Returns:
        dict with keys: invested, returns, total
    """
    total   = principal * ((1 + rate / 400) ** (4 * time))
    returns = total - principal
    return {
        "invested": round(principal, 2),
        "returns":  round(returns, 2),
        "total":    round(total, 2),
    }


def calculate_all_banks(principal: float, years: float, banks: list) -> list:
    """
    Calculate FD returns for every bank and return results sorted best-first.

    Each item in the returned list contains:
        name, logo, tagline, booking_url, rate, returns, total

    Args:
        principal: Investment amount (₹)
        years:     Duration in years
        banks:     List of bank dicts loaded from fd_data.json
    """
    results = []
    for bank in banks:
        rate = _best_rate_for_tenure(bank["rates"], years)
        calc = calculate_fd(principal, rate, years)
        results.append({
            "name":        bank["name"],
            "logo":        bank.get("logo", "🏦"),
            "tagline":     bank.get("tagline", ""),
            "booking_url": bank.get("booking_url", "#"),
            "rate":        rate,
            "returns":     calc["returns"],
            "total":       calc["total"],
        })
    # Primary sort: highest total first. Secondary: alphabetical by name (tie-breaker).
    results.sort(key=lambda x: (-x["total"], x["name"]))
    return results


def _best_rate_for_tenure(rates: dict, years: float) -> float:
    """
    Pick the closest available rate for the requested tenure.
    In case of a tie, the shorter (more conservative) tenure is used.
    """
    available = {float(k): v for k, v in rates.items()}
    best_key  = min(available.keys(), key=lambda t: abs(t - years))
    return available[best_key]