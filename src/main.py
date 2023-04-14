from fastapi import FastAPI

from src.controllers import posts
from src.database import Base, engine

app = FastAPI()
app.include_router(posts.router)


@app.get("/")
def index():
    return "Hello World"


Base.metadata.create_all(engine)
