from fastapi import APIRouter, HTTPException

from src.deposit.calculation import Calculation
from src.deposit.schema import DepositBase

router = APIRouter(
    prefix="/deposit",
    tags=["Deposit"]
)
calculation = Calculation()


@router.post("/")
async def post_deposit(data: DepositBase) -> dict:
    try:
        result = await calculation.cal_date(dict(data))
        return result
    except Exception as error:
        raise HTTPException(status_code=500,
                            detail=
                            {
                                "error": error
                            })
