from fastapi import FastAPI, Request
from pydantic import BaseModel
from models import train_model
from utils import mask_pii
import joblib
import os

app = FastAPI()

if not os.path.exists("model/classifier.pkl"):
    train_model()

model = joblib.load("model/classifier.pkl")

class EmailRequest(BaseModel):
    email: str

@app.post("/classify")
def classify_email(data: EmailRequest):
    masked_email, pii_entities, _ = mask_pii(data.email)
    category = model.predict([masked_email])[0]

    return {
        "input_email_body": data.email,
        "list_of_masked_entities": pii_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
