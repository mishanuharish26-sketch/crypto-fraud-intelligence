from blockchain.ethereum.risk_analysis import calculate_risk_score


def test_low_risk():
    result = calculate_risk_score(
        traced_transfers=5,
        unique_counterparties=2,
        max_hop=1,
        high_value_count=1,
    )

    assert result["score"] == 0
    assert result["level"] == "LOW"


def test_critical_risk():
    result = calculate_risk_score(
        traced_transfers=25,
        unique_counterparties=12,
        max_hop=4,
        high_value_count=6,
    )

    assert result["score"] == 85
    assert result["level"] == "CRITICAL"