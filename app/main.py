import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {"hello"}




if __name__ == "__main__":
    uvicorn.run(app)