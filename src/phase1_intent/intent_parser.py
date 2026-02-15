import re
from typing import List, Tuple, Optional
from src.phase1_intent.schema import UserIntent, RiskConfig
from src.utils.text_cleaner import clean_text


class IntentParser:

    def parse(self, raw_text: str) -> UserIntent:
        text = clean_text(raw_text)

        assets, weights = self._extract_portfolio(text)
        years = self._extract_years(text)
        frequency = self._extract_frequency(text)
        risk = self._extract_risk(text)
        flags = self._extract_flags(text)

        return UserIntent(
            assets=assets if assets else ['NIFTY50'],
            weights=weights if weights else [1.0],
            data_frequency=frequency,
            start_year=years[0],
            end_year=years[1],
            risk=risk,
            backtesting=flags['backtesting'],
            explain=flags['explain']
        )

    def _extract_portfolio(self, text: str) -> Tuple[List[str], List[float]]:
        patterns = [
            r'([A-Z][A-Z0-9]*(?:\s+[A-Z0-9]+)?)\s*\(?(\d+(?:\.\d+)?)\s*percent?\)?',
            r'([A-Z][A-Z0-9]*)\s*\((\d+(?:\.\d+)?)\s*%\)',
            r'([A-Z][A-Z0-9]*)\s+(\d+(?:\.\d+)?)\s*percent'
        ]

        assets = []
        weights = []

        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for asset, pct in matches:
                asset_name = re.sub(r'\s+', '_', asset.strip().upper())
                if asset_name not in assets:
                    assets.append(asset_name)
                    weights.append(float(pct) / 100.0)

        if weights:
            total = sum(weights)
            weights = [w / total for w in weights]

        return assets, weights

    def _extract_years(self, text: str) -> Tuple[int, int]:
        years = re.findall(r'20\d{2}', text)
        if len(years) >= 2:
            return int(years[0]), int(years[1])
        return 2020, 2024

    def _extract_frequency(self, text: str) -> str:
        match = re.search(r'(daily|weekly|monthly)', text, re.IGNORECASE)
        if match:
            return match.group(1)
        return 'daily'

    def _extract_risk(self, text: str) -> Optional[RiskConfig]:
        text_lower = text.lower()

        if 'var' not in text_lower:
            return None

        confidence = 0.99 if '99' in text else 0.95
        horizon = 10 if '10' in text else 1

        models = []

        if 'historical' in text_lower:
            models.append('historical')

        if any(term in text_lower for term in ['variance', 'covariance', 'var-cov']):
            models.append('varcov')

        if 'monte' in text_lower:
            models.append('monte_carlo')

        if not models:
            return None

        return RiskConfig(
            confidence=confidence,
            horizon_days=horizon,
            models=models
        )

    def _extract_flags(self, text: str) -> dict:
        text_lower = text.lower()

        return {
            'backtesting': any(term in text_lower for term in ['backtest', 'back-test', 'backtesting']),
            'explain': 'explain' in text_lower
        }
