import uvicorn
from fastapi import FastAPI
from routers import main
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main.router)



if __name__ == "__main__":
    uvicorn.run(app)