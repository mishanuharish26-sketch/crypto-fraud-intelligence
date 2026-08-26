from fraud_detection.detector import analyze_fraud


def test_suspicious_activity():
    result = analyze_fraud(
        traced_transfers=25,
        unique_counterparties=12,
        max_hop=4,
        high_value_count=6,
    )

    assert result["suspicious"] is True
    assert result["confidence"] == 0.9
    assert len(result["patterns"]) == 4


def test_low_activity():
    result = analyze_fraud(
        traced_transfers=3,
        unique_counterparties=2,
        max_hop=1,
        high_value_count=0,
    )

    assert result["suspicious"] is False
    assert len(result["patterns"]) == 0