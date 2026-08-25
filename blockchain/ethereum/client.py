import requests

from .config import ALCHEMY_API_KEY


ALCHEMY_URL = (
    f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
)


def get_eth_balance(wallet_address: str) -> float:
    """Return the ETH balance of a wallet."""

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1,
    }

    response = requests.post(
        ALCHEMY_URL,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()

    result = response.json()

    if "error" in result:
        raise RuntimeError(result["error"])

    wei_balance = int(result["result"], 16)
    return wei_balance / 10**18


def get_transfers(wallet_address: str) -> list[dict]:
    """Retrieve Ethereum asset transfers involving a wallet."""

    payload = {
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [
            {
                "fromBlock": "0x0",
                "toBlock": "latest",
                "fromAddress": wallet_address,
                "excludeZeroValue": True,
                "withMetadata": True,
                "maxCount": "0x64",
                "category": [
                    "external",
                    "internal",
                    "erc20",
                    "erc721",
                    "erc1155"
                ]
            }
        ],
        "id": 1
    }

    response = requests.post(
        ALCHEMY_URL,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()

    result = response.json()

    if "error" in result:
        raise RuntimeError(result["error"])

    return result.get("result", {}).get("transfers", [])


if __name__ == "__main__":
    test_wallet = "0x0000000000000000000000000000000000000000"

    print("Ethereum connection successful.")

    balance = get_eth_balance(test_wallet)
    print(f"Test wallet: {test_wallet}")
    print(f"ETH balance: {balance}")

    transfers = get_transfers(test_wallet)

    print(f"Transfers found: {len(transfers)}")

    for transfer in transfers[:5]:
        print(
            transfer.get("from"),
            "->",
            transfer.get("to"),
            "|",
            transfer.get("value"),
            transfer.get("asset")
        )