from typing import List, Optional
from pydantic import BaseModel

class Tax(BaseModel):
    taxType: str
    taxId: str
    rate: int

class Price(BaseModel):
    fullPrice: int
    taxes: Optional[List[Tax]]

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
    price: Optional[Price]
    points: int

class ClientPortfolio(BaseModel):
    channel: str
    country: str
    createdDate: str
    customerCode: str
    items: Optional[List[Item]]
    route: str
