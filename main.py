from fastapi import FastAPI, Request, Response
from .app.users.router import router as userRouter
from .app.middleware.auth_middleware import authorize

app = FastAPI()

excluded_urls = [
    '/users/login',
]

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if(request.url.path in excluded_urls):
        return await call_next(request)

    if not await authorize(request.headers):
        return Response("Unauthorized", status_code=401)
    else:
        response = await call_next(request)
        print(response)
        return response


app.include_router(userRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}


