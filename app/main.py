from fastapi import FastAPI
from app.api.routes import router as client_portfolio_router

app = FastAPI()

app.include_router(client_portfolio_router, prefix="/api")
