from fastapi import FastAPI

from src import models
from src.controllers import posts
from src.database import engine

app = FastAPI()
app.include_router(posts.router)


@app.get("/")
def index():
    return "Hello World"


models.Base.metadata.create_all(engine)
