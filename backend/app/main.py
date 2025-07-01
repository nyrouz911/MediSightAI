#STARTS THE FASTAPI APP

from fastapi import FastAPI
from app.api import v1

app = FastAPI(title="MediSightAI")

app.include_router(v1.router)
