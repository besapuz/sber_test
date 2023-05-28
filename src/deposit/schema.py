from pydantic import BaseModel, Field, validator
from datetime import datetime, date


class DepositBase(BaseModel):
    date: str = datetime.strptime('2023-25-3', '%Y-%d-%m').strftime('%d.%m.%Y')
    periods: int = Field(ge=1, le=60)
    amount: int = Field(ge=10_000, le=3_000_000)
    rate: float = Field(ge=1, le=8)

    @validator("date")
    def validate_date(cls, value) -> date:
        return datetime.strptime(str(value), '%d.%m.%Y').strftime('%d.%m.%Y')

