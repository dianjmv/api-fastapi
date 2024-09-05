from typing import List, Optional
from pydantic import BaseModel

class TaxSchema(BaseModel):
    taxType: str
    taxId: str
    rate: int

class PriceSchema(BaseModel):
    fullPrice: int
    taxes: List[TaxSchema]

class ItemSchema(BaseModel):
    sku: str
    title: str
    categoryId: str
    category: str
    brand: str
    classification: str
    unitsPerBox: str
    minOrderUnits: str
    packageDescription: str
    packageUnitDescription: str
    quantityMaxRedeem: int
    redeemUnit: str
    orderReasonRedeem: str
    skuRedeem: bool
    price: PriceSchema
    points: int

class ClientPortfolioSchema(BaseModel):
    id: Optional[str]
    channel: str
    country: str
    createdDate: str
    customerCode: str
    items: List[ItemSchema]
    route: str
