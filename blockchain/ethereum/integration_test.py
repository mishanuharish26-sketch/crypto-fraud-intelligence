from .fund_flow import trace_live_fund_flow
from .graph import build_transaction_graph, graph_summary


def main():
    # Small, controlled test
    test_wallet = "0x0000000000000000000000000000000000000000"

    print("Starting live CryptoTrace integration test...")
    print(f"Wallet: {test_wallet}")

    traced = trace_live_fund_flow(
        start_wallet=test_wallet,
        max_hops=1,
        min_value=100.0,
    )

    print(f"Transfers traced: {len(traced)}")

    graph = build_transaction_graph(traced)

    summary = graph_summary(graph)

    print("Graph summary:")
    print(summary)

    print("\nFirst 5 graph edges:")

    for edge in graph["edges"][:5]:
        print(
            f"{edge['from']} -> {edge['to']} | "
            f"{edge['value']} {edge['asset']} | "
            f"hop={edge['hop']}"
        )


if __name__ == "__main__":
    main()