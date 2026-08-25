from collections import deque
from typing import Any

from .client import get_transfers
from .parser import normalize_transfer


def trace_live_fund_flow(
    start_wallet: str,
    max_hops: int = 3,
    min_value: float = 0.0,
) -> list[dict[str, Any]]:
    """
    Trace outgoing Ethereum transfers across multiple wallets.

    The tracer:
    - starts from the reported wallet
    - retrieves live transfers from Alchemy
    - normalizes each transfer
    - follows destination wallets
    - stops at max_hops
    - avoids cycles and duplicate transactions
    """

    queue = deque([(start_wallet.lower(), 0)])
    visited_wallets = {start_wallet.lower()}
    seen_transactions = set()
    traced_edges = []

    while queue:
        current_wallet, hop = queue.popleft()

        if hop >= max_hops:
            continue

        transfers = get_transfers(current_wallet)

        for raw_transfer in transfers:
            tx = normalize_transfer(raw_transfer)

            tx_hash = tx.get("hash")
            sender = (tx.get("from") or "").lower()
            receiver = (tx.get("to") or "").lower()
            value = tx.get("value")

            if not receiver:
                continue

            if sender != current_wallet:
                continue

            if tx_hash and tx_hash in seen_transactions:
                continue

            if value is None:
                continue

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                continue

            if numeric_value < min_value:
                continue

            if tx_hash:
                seen_transactions.add(tx_hash)

            edge = {
                "from": tx.get("from"),
                "to": tx.get("to"),
                "value": numeric_value,
                "asset": tx.get("asset"),
                "hash": tx.get("hash"),
                "category": tx.get("category"),
                "blockNumber": tx.get("blockNumber"),
                "timestamp": tx.get("timestamp"),
                "hop": hop + 1,
            }

            traced_edges.append(edge)

            if receiver not in visited_wallets:
                visited_wallets.add(receiver)
                queue.append((receiver, hop + 1))

    return traced_edges


if __name__ == "__main__":
    test_wallet = "0x0000000000000000000000000000000000000000"

    results = trace_live_fund_flow(
        start_wallet=test_wallet,
        max_hops=2,
        min_value=100.0,
    )

    print(f"Traced transfers: {len(results)}")

    for item in results[:10]:
        print(
            f"Hop {item['hop']}: "
            f"{item['from']} -> {item['to']} | "
            f"{item['value']} {item['asset']}"
        )