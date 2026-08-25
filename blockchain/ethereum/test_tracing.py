from parser import trace_fund_flow


sample_transactions = [
    {
        "hash": "0x111",
        "from": "0xAAA",
        "to": "0xBBB",
        "value": 100.0,
        "asset": "ETH",
    },
    {
        "hash": "0x222",
        "from": "0xBBB",
        "to": "0xCCC",
        "value": 80.0,
        "asset": "ETH",
    },
    {
        "hash": "0x333",
        "from": "0xCCC",
        "to": "0xDDD",
        "value": 60.0,
        "asset": "ETH",
    },
    {
        "hash": "0x444",
        "from": "0xDDD",
        "to": "0xEEE",
        "value": 40.0,
        "asset": "ETH",
    },
]


result = trace_fund_flow(
    sample_transactions,
    start_wallet="0xAAA",
    max_hops=3,
    min_value=50.0,
)

print("Traced fund flow:")

for edge in result:
    print(
        f"Hop {edge['hop']}: "
        f"{edge['from']} -> {edge['to']} | "
        f"{edge['value']} {edge['asset']}"
    )