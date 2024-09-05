from typing import List
from app.config import database
from app.core.models import ClientPortfolio
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

collection: AsyncIOMotorCollection = database.get_collection("client-portfolio")

async def get_all_client_portfolios() -> List[ClientPortfolio]:
    client_portfolios = []
    async for client_portfolio in collection.find():
        client_portfolios.append(ClientPortfolio(**client_portfolio))
    return client_portfolios

async def get_client_portfolio_by_id(id: str) -> ClientPortfolio:
    client_portfolio = await collection.find_one({"_id": ObjectId(id)})
    if client_portfolio:
        return ClientPortfolio(**client_portfolio)

async def create_client_portfolio(client_portfolio: ClientPortfolio) -> ClientPortfolio:
    result = await collection.insert_one(client_portfolio.dict())
    return ClientPortfolio(**client_portfolio.dict(), id=str(result.inserted_id))

async def delete_client_portfolio(id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
