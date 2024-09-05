from typing import List
from app.core.models import ClientPortfolio
from app.repositories import client_portfolio_repository as repository

async def get_all_client_portfolios() -> List[ClientPortfolio]:
    return await repository.get_all_client_portfolios()

async def get_client_portfolio_by_id(id: str) -> ClientPortfolio:
    return await repository.get_client_portfolio_by_id(id)

async def create_client_portfolio(client_portfolio: ClientPortfolio) -> ClientPortfolio:
    return await repository.create_client_portfolio(client_portfolio)

async def delete_client_portfolio(id: str) -> bool:
    return await repository.delete_client_portfolio(id)
