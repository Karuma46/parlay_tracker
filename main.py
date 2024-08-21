from fastapi import FastAPI
from .app.users.router import router as userRouter
from .app.teams.router import router as teamRouter
from .app.parlays.router import router as parlayRouter
from .app.middleware.auth_middleware import AuthMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://127.0.0.1",
    "http://localhost:5173",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(AuthMiddleware)


app.include_router(userRouter)
app.include_router(teamRouter)
app.include_router(parlayRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}


