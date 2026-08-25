from collections import deque
from typing import Any


def normalize_transfer(transfer: dict[str, Any]) -> dict[str, Any]:
    """Convert an Alchemy transfer into CryptoTrace's common format."""

    metadata = transfer.get("metadata") or {}

    return {
        "hash": transfer.get("hash"),
        "from": transfer.get("from"),
        "to": transfer.get("to"),
        "value": transfer.get("value"),
        "asset": transfer.get("asset"),
        "category": transfer.get("category"),
        "blockNumber": transfer.get("blockNum"),
        "timestamp": metadata.get("blockTimestamp"),
    }


def normalize_transfers(
    transfers: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Normalize a list of Alchemy transfers."""

    return [normalize_transfer(transfer) for transfer in transfers]


def trace_fund_flow(
    transactions: list[dict[str, Any]],
    start_wallet: str,
    max_hops: int = 3,
    min_value: float = 0.0,
) -> list[dict[str, Any]]:
    """
    Trace outgoing fund movement using bounded BFS.
    """

    queue = deque([(start_wallet.lower(), 0)])
    visited = {start_wallet.lower()}
    traced_edges: list[dict[str, Any]] = []

    while queue:
        current_wallet, hop_count = queue.popleft()

        if hop_count >= max_hops:
            continue

        for tx in transactions:
            sender = (tx.get("from") or "").lower()
            receiver = (tx.get("to") or "").lower()
            value = tx.get("value")

            if sender != current_wallet:
                continue

            if value is None:
                continue

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                continue

            if numeric_value < min_value:
                continue

            traced_edges.append(
                {
                    "from": tx.get("from"),
                    "to": tx.get("to"),
                    "value": numeric_value,
                    "asset": tx.get("asset"),
                    "hash": tx.get("hash"),
                    "hop": hop_count + 1,
                }
            )

            if receiver and receiver not in visited:
                visited.add(receiver)
                queue.append((receiver, hop_count + 1))

    return traced_edges