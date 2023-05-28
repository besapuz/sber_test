from datetime import datetime, date

from loguru import logger
from dateutil.relativedelta import relativedelta


class Calculation:
    async def calculates_interest(self, data: dict):
        try:
            date_: date = datetime.strptime(data["date"], '%d.%m.%Y').date()
            mount = data["periods"]
            for i in range(mount):
                day = date_ + relativedelta(months=+i+1)
                logger.info(datetime.strptime(str(day), '%Y-%m-%d').strftime('%d.%m.%Y'))
        except Exception as error:
            logger.error(error)

