from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PredType(BaseModel):

    time_horizon: int
    time_fraction: Optional[float]
    #historic_point: Optional[str]
