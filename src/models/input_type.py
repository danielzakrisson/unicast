from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PredType(BaseModel):
    
    lower_bound: Optional[float]
    upper_bound: Optional[float]
    time_horizon: int
    time_fraction: Optional[float]
    #historic_point: Optional[str]
    prediction_type: Optional[str] = "Expected_timefraction"
