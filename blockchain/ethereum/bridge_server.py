import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from .fund_flow import trace_live_fund_flow
from .graph import build_transaction_graph, graph_summary


class BridgeHandler(BaseHTTPRequestHandler):

    def _send_json(self, data: dict, status: int = 200):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send_json({
                "status": "ok",
                "service": "CryptoTrace Python Blockchain Bridge"
            })
            return

        self._send_json(
            {"error": "Endpoint not found"},
            404
        )

    def do_POST(self):
        if self.path != "/analyze":
            self._send_json(
                {"error": "Endpoint not found"},
                404
            )
            return

        try:
            content_length = int(
                self.headers.get("Content-Length", "0")
            )

            raw_body = self.rfile.read(content_length)
            request_data = json.loads(raw_body)

            wallet_address = request_data.get("walletAddress")

            if not wallet_address:
                self._send_json(
                    {"error": "walletAddress is required"},
                    400
                )
                return

            traced = trace_live_fund_flow(
                start_wallet=wallet_address,
                max_hops=1,
                min_value=100.0
            )

            graph = build_transaction_graph(traced)
            summary = graph_summary(graph)

            self._send_json({
                "walletAddress": wallet_address,
                "tracedTransfers": len(traced),
                "graph": summary,
                "edges": graph["edges"][:20]
            })

        except Exception as exc:
            self._send_json(
                {"error": str(exc)},
                500
            )


if __name__ == "__main__":
    server = HTTPServer(
        ("127.0.0.1", 5000),
        BridgeHandler
    )

    print(
        "CryptoTrace Python bridge started on "
        "http://127.0.0.1:5000"
    )
    print("Health: GET /health")
    print("Analyze: POST /analyze")

    server.serve_forever()