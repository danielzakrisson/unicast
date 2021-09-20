from pydantic import BaseModel

class PredType(BaseModel):
    lower_bound: float
    upper_bound: float
    time_horizon: int
