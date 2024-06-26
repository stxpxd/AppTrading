from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_some():
    return "start"


