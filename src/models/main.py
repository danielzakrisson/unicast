from src.models.expected_timefraction_predictions import best_range
from src.models import input_type

import uvicorn
from fastapi import FastAPI, Header, File, UploadFile
from pydantic import BaseModel
import json

app = FastAPI()
PredType = input_type.PredType


@app.get("/")
def read_root():
    return {"UniCast": "Optimize your Uniswap settings"}


@app.post("/best_range")
def best_range_(inp_request: PredType = None):
    timefraction = inp_request.time_fraction
    time_horizon = inp_request.time_horizon
    res, metadata = best_range(timefraction, time_horizon)
    return json.dumps(res)


if __name__ == '__main__':
    #uvicorn.run(app, port=8000)
    uvicorn.run(app, port=8000, host="0.0.0.0")