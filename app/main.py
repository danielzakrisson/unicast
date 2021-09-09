from typing import Optional
import numpy as np
from import_etherium_timeseries import etherium_data
from expected_timefraction_predictions import expected_timefraction

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/timefraction_prediction")
def home(lower_bound: float, upper_bound: float, time_horizon: int):

    timefrac = expected_timefraction(lower_bound, upper_bound, time_horizon)
    return {'Expected_timefraction': timefrac}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")