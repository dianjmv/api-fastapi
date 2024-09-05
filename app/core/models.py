from typing import List
from pydantic import BaseModel

class Tax(BaseModel):
    taxType: str
    taxId: str
    rate: int

class Price(BaseModel):
    fullPrice: int
    taxes: List[Tax]

class Item(BaseModel):
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
    price: Price
    points: int

class ClientPortfolio(BaseModel):
    channel: str
    country: str
    createdDate: str
    customerCode: str
    items: List[Item]
    route: str
