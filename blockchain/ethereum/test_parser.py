from parser import normalize_transfer


sample_transfer = {
    "hash": "0xabc123",
    "from": "0x1111111111111111111111111111111111111111",
    "to": "0x2222222222222222222222222222222222222222",
    "value": 1.5,
    "asset": "ETH",
    "category": "external",
    "blockNum": "0x123456",
    "metadata": {
        "blockTimestamp": "2026-08-25T12:00:00.000Z"
    }
}

result = normalize_transfer(sample_transfer)

print("Normalized transaction:")
print(result)