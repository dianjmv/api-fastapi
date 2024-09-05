from fastapi import APIRouter, HTTPException
from typing import List
from app.core.schemas import ClientPortfolioSchema
from app.core import services

router = APIRouter()

@router.get("/client-portfolio")
async def get_all_client_portfolios():
    return await services.get_all_client_portfolios()

@router.get("/client-portfolio/{id}")
async def get_client_portfolio_by_id(id: str):
    client_portfolio = await services.get_client_portfolio_by_id(id)
    if client_portfolio is None:
        raise HTTPException(status_code=404, detail="Client Portfolio not found")
    return client_portfolio

@router.post("/client-portfolio")
async def create_client_portfolio(client_portfolio: ClientPortfolioSchema):
    return await services.create_client_portfolio(client_portfolio)

@router.delete("/client-portfolio/{id}", response_model=bool)
async def delete_client_portfolio(id: str):
    return await services.delete_client_portfolio(id)
