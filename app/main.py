import uvicorn
from fastapi import FastAPI
from routers import main


app = FastAPI()


app.include_router(main.router)



if __name__ == "__main__":
    uvicorn.run(app)