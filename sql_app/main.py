import fastapi

app = fastapi.FastAPI()


@app.get("/")
def home():
    return {"Message": "Hello world"}
