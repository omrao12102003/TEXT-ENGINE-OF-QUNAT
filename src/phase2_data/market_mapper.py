ASSET_MAP = {
    "NIFTY50": "^NSEI",     # NIFTY 50 Index
    "SP500": "^GSPC",       # S&P 500
    "NASDAQ": "^IXIC",      # NASDAQ Composite
    "DOW": "^DJI",          # Dow Jones
    "BITCOIN": "BTC-USD",   # Bitcoin USD
    "BTC": "BTC-USD"        # Alias support
}

def map_assets(assets: list) -> dict:
    mapped = {}

    for asset in assets:
        clean_asset = asset.replace('WITH_', '').upper()

        if clean_asset in ASSET_MAP:
            mapped[asset] = ASSET_MAP[clean_asset]
        else:
            print(f"Unknown asset: {asset}")

    return mapped

