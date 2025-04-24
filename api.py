import gradio as gr
from models import train_model
from utils import mask_pii
import joblib
import os

# Train if model is missing
if not os.path.exists("model/classifier.pkl"):
    train_model()

# Load the model
model = joblib.load("model/classifier.pkl")

def classify_email(email):
    masked_email, pii_entities, _ = mask_pii(email)
    category = model.predict([masked_email])[0]
    
    return email, str(pii_entities), masked_email, category

# Define Gradio API endpoint
def create_gradio_api():
    api = gr.Interface(
        fn=classify_email,
        inputs=gr.Textbox(lines=10, label="Enter Email"),
        outputs=[
            gr.Textbox(label="Input Email Body"),
            gr.Textbox(label="List of Masked Entities"),
            gr.Textbox(label="Masked Email"),
            gr.Textbox(label="Category of the Email")
        ],
        title="Email Classifier with PII Masking",
        description="Classifies email content and masks personally identifiable information (PII).",
        live=True,
    )

    return api
