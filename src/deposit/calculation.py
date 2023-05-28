from datetime import datetime, date

from loguru import logger
from dateutil.relativedelta import relativedelta


class Calculation:
    def __cal_interest(self, amount: int | float, rate: float) -> float:
        ratio: float = rate / 12 / 100 + 1
        result: float = amount * ratio
        amount: float = round(result, 2)
        return amount

    async def cal_date(self, data: dict) -> dict:
        example = {}
        try:
            date_: date = datetime.strptime(data["date"], '%d.%m.%Y').date()
            mount: int = data["periods"]
            cal: float = Calculation.__cal_interest(self, data["amount"], data["rate"])
            for i in range(mount):
                next_mount: str = datetime.strptime(str(date_ + relativedelta(months=+i+1)), '%Y-%m-%d').strftime('%d.%m.%Y')
                example[next_mount] = cal
                cal: float = Calculation.__cal_interest(self, cal, data["rate"])
            return example
        except Exception as error:
            logger.error(error)




