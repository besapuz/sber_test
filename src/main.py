from fastapi import FastAPI
import uvicorn
from src.deposit.routes import router as router_deposit

app = FastAPI()

app.include_router(router_deposit)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)

