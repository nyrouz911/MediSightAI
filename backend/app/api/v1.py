#API ENDPOINT

from fastapi import APIRouter
from app.services import nlp_service

router = APIRouter()

@router.post("/analyze")
async def analyze_symptoms(symptoms: dict):
    text = symptoms.get("text", "")
    result = nlp_service.classify_symptoms(text)
    return {"result": result}
