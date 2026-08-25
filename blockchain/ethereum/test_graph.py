from graph import build_transaction_graph, graph_summary


sample_transactions = [
    {
        "hash": "0x111",
        "from": "0xAAA",
        "to": "0xBBB",
        "value": 100.0,
        "asset": "ETH",
        "category": "external",
        "hop": 1,
    },
    {
        "hash": "0x222",
        "from": "0xBBB",
        "to": "0xCCC",
        "value": 80.0,
        "asset": "ETH",
        "category": "external",
        "hop": 2,
    },
    {
        "hash": "0x333",
        "from": "0xCCC",
        "to": "0xDDD",
        "value": 60.0,
        "asset": "ETH",
        "category": "external",
        "hop": 3,
    },
]


graph = build_transaction_graph(sample_transactions)

print("Graph summary:")
print(graph_summary(graph))

print("\nNodes:")
for node in graph["nodes"]:
    print(node)

print("\nEdges:")
for edge in graph["edges"]:
    print(edge)