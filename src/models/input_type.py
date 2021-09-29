from pydantic import BaseModel
from typing import Optional

class PredType(BaseModel):
    
    lower_bound: Optional[float]
    upper_bound: Optional[float]
    time_horizon: int
    time_fraction: Optional[float]
    prediction_type: Optional[str]
