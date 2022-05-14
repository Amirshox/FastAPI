import uvicorn
from fastapi import FastAPI
from db import database
from routes import router
from sql_tables import create_tables

app = FastAPI()


@app.on_event("startup")
async def startup():
    await create_tables()
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router=router)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
