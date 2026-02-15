class LLMClient:
    """
    Simple LLM interface used for generating executive reports.
    This version contains a deterministic mock implementation.
    """

    def generate(self, prompt: str) -> str:
        """
        Returns a predefined executive report based on prompt content.
        """

        if "breaches: Historical=0" in prompt and "Green" in prompt:
            return (
                "EXECUTIVE RISK SUMMARY:\n"
                "The NIFTY50 portfolio shows a 10-day VaR of approximately 7.4–7.5% "
                "at 99% confidence across all models.\n\n"
                "MODEL RELIABILITY ASSESSMENT:\n"
                "Historical, VaR-Covariance, and Monte Carlo methods show close alignment, "
                "indicating consistent risk estimation.\n\n"
                "TAIL RISK INTERPRETATION:\n"
                "Expected Shortfall is consistent with VaR estimates, suggesting limited "
                "additional tail exposure beyond the threshold.\n\n"
                "REGULATORY STATUS:\n"
                "All models report zero breaches over 1826 observations, "
                "indicating compliance with Basel green zone standards.\n\n"
                "CRO RECOMMENDATION:\n"
                "Monte Carlo VaR may be used as the primary reporting measure. "
                "Periodic backtesting is recommended."
            )

        return (
            "EXECUTIVE RISK SUMMARY:\n"
            "The portfolio shows a stable risk profile across models.\n\n"
            "MODEL RELIABILITY ASSESSMENT:\n"
            "VaR estimates are consistent across methodologies.\n\n"
            "TAIL RISK INTERPRETATION:\n"
            "Expected Shortfall indicates manageable tail risk.\n\n"
            "REGULATORY STATUS:\n"
            "Backtesting results are within acceptable limits.\n\n"
            "CRO RECOMMENDATION:\n"
            "The current framework is suitable for continued monitoring."
        )
