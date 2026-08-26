def calculate_risk_score(
    traced_transfers: int,
    unique_counterparties: int,
    max_hop: int,
    high_value_count: int,
) -> dict:
    score = 0
    reasons = []

    if traced_transfers >= 20:
        score += 25
        reasons.append("High number of traced transfers")

    if unique_counterparties >= 10:
        score += 20
        reasons.append("Many unique counterparties")

    if max_hop >= 3:
        score += 20
        reasons.append("Multi-hop fund movement")

    if high_value_count >= 5:
        score += 20
        reasons.append("Multiple high-value transfers")

    if score >= 80:
        level = "CRITICAL"
    elif score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": min(score, 100),
        "level": level,
        "reasons": reasons,
    }