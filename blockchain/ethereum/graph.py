from typing import Any


def build_transaction_graph(
    transactions: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Build a simple transaction graph.

    Nodes = wallet addresses
    Edges = transfers between wallets
    """

    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []

    for tx in transactions:
        sender = tx.get("from")
        receiver = tx.get("to")

        if not sender or not receiver:
            continue

        sender = sender.lower()
        receiver = receiver.lower()

        # Add sender node
        if sender not in nodes:
            nodes[sender] = {
                "id": sender,
                "type": "wallet",
            }

        # Add receiver node
        if receiver not in nodes:
            nodes[receiver] = {
                "id": receiver,
                "type": "wallet",
            }

        # Add transfer edge
        edges.append(
            {
                "from": sender,
                "to": receiver,
                "hash": tx.get("hash"),
                "value": tx.get("value"),
                "asset": tx.get("asset"),
                "category": tx.get("category"),
                "blockNumber": tx.get("blockNumber"),
                "timestamp": tx.get("timestamp"),
                "hop": tx.get("hop"),
            }
        )

    return {
        "nodes": list(nodes.values()),
        "edges": edges,
    }


def graph_summary(graph: dict[str, Any]) -> dict[str, int]:
    """Return basic graph statistics."""

    return {
        "nodeCount": len(graph.get("nodes", [])),
        "edgeCount": len(graph.get("edges", [])),
    }