from typing import Optional
import numpy as np
from src.models.import_ethereum_timeseries import ethereum_data
from src.models.expected_timefraction_predictions import expected_timefraction

#from import_ethereum_timeseries import ethereum_data
#from expected_timefraction_predictions import expected_timefraction


from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from src.models import predict

from fastapi import FastAPI, Header, File, UploadFile
from typing import List, Optional
from pydantic import BaseModel
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"UniCast": "Optimize your Uniswap settings"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/timefraction_prediction")
def home(lower_bound: float, upper_bound: float, time_horizon: int):

    timefrac = expected_timefraction(lower_bound, upper_bound, time_horizon)
    return {'Expected_timefraction': timefrac}


try:
    from src.models import input_type

    PredType = input_type.PredType
    print('User defined input type.')
except:
    print('Using default input type.')


    class PredType(BaseModel):
        pred: str

try:
    from src.models import input_type
    defv = input_type.defv
except:
    defv = None

model_data = []
if hasattr(predict, 'model_load'):
    print('Loading model...')
    model_data = predict.model_load()
    print('Done.')


@app.post("/timefraction_prediction")
def model_predict(lower_bound: float, upper_bound: float, time_horizon: int):

    timefrac = expected_timefraction(lower_bound, upper_bound, time_horizon)
    return {'Expected_timefraction': timefrac}


@app.post("/predict/")
async def predict_route(pred_request: PredType = defv, X_Auth_Username: Optional[List[str]] = Header(None)):
    print('Username: {}'.format(X_Auth_Username))
    print(pred_request)
    res = predict.model_predict(pred_request, model_data)
    return json.dumps(res)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")