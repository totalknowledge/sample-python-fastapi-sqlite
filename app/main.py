from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers.user_router import router as user_router

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def read_root(request: Request):
    base_url = str(request.base_url)
    return {
        "message": "Welcome to the FastAPI User Management API",
        "docs": {
            "Swagger UI": {
                "description": "Interactive API documentation and testing",
                "link": base_url + "docs"
            },
            "ReDoc": {
                "description": "Alternative API documentation",
                "link": base_url + "redoc"
            }
        }
    }

app.include_router(user_router)
