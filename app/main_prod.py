from fastapi import FastAPI
from pydantic import BaseModel
from model_prod import predict

app = FastAPI(title="ML FastAPI Service")


class InputData(BaseModel):
    features: list[float]


@app.post("/predict")
async def get_prediction(data: InputData):
    prediction = predict(data.features)
    return {"prediction": prediction}