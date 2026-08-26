def extract_features(
    traced_transfers: int,
    unique_counterparties: int,
    max_hop: int,
    high_value_count: int,
) -> dict:
    return {
        "traced_transfers": traced_transfers,
        "unique_counterparties": unique_counterparties,
        "max_hop": max_hop,
        "high_value_count": high_value_count,
    }