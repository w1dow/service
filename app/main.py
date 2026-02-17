from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_hello():
    return "Hello, this is me"

@app.get("/bye")
def read_bye():
    return "Good bye"
