from fastapi import APIRouter

from src.deposit.calculation import Calculation
from src.deposit.schema import DepositBase

router = APIRouter(
    prefix="/deposit",
    tags=["Deposit"]
)
calculation = Calculation()


@router.get("/")
async def get_deposit():
    return "work"


@router.post("/")
async def post_deposit(data: DepositBase):
    return await calculation.calculates_interest(dict(data))
