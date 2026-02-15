from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class RiskConfig(BaseModel):
    confidence: float = Field(..., ge=0.9, le=0.999)
    horizon_days: int = Field(..., ge=1, le=365)
    models: List[str] = []
    expected_shortfall: bool = False

class UserIntent(BaseModel):
    assets: List[str]
    weights: List[float]
    data_frequency: str = "daily"
    start_year: int = Field(..., ge=2000, le=date.today().year)
    end_year: int = Field(..., ge=2000, le=date.today().year)
    risk: Optional[RiskConfig] = None
    backtesting: bool = False
    explain: bool = False
