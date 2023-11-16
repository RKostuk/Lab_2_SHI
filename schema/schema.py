from pydantic import BaseModel

class DataResponse(BaseModel):
    work: str
    price: str
    screen: int
    weight: str
    brand: str