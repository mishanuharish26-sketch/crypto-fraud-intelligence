def detect_rules(
    traced_transfers: int,
    unique_counterparties: int,
    max_hop: int,
    high_value_count: int,
):
    alerts = []

    if traced_transfers >= 20:
        alerts.append({
            "pattern": "High transaction activity",
            "reason": "Large number of traced transfers"
        })

    if unique_counterparties >= 10:
        alerts.append({
            "pattern": "Many counterparties",
            "reason": "Wallet interacts with many different addresses"
        })

    if max_hop >= 3:
        alerts.append({
            "pattern": "Layering",
            "reason": "Funds move through multiple intermediary wallets"
        })

    if high_value_count >= 5:
        alerts.append({
            "pattern": "High-value movement",
            "reason": "Multiple high-value transfers detected"
        })

    return alerts