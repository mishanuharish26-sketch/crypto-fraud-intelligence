from fraud_detection.rules import detect_rules
from fraud_detection.features import extract_features


def analyze_fraud(
    traced_transfers: int,
    unique_counterparties: int,
    max_hop: int,
    high_value_count: int,
) -> dict:

    features = extract_features(
        traced_transfers,
        unique_counterparties,
        max_hop,
        high_value_count,
    )

    alerts = detect_rules(
        traced_transfers,
        unique_counterparties,
        max_hop,
        high_value_count,
    )

    suspicious = len(alerts) > 0

    confidence = min(
        0.50 + (len(alerts) * 0.10),
        0.90
    )

    return {
        "suspicious": suspicious,
        "confidence": round(confidence, 2),
        "features": features,
        "patterns": alerts,
    }