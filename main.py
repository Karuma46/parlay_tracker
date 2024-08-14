from fastapi import FastAPI
from .app.users.router import router as userRouter

app = FastAPI()
app.include_router(userRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}


