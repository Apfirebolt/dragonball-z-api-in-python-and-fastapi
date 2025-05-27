from fastapi import FastAPI, Request
import uvicorn
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from api import router as api_router
from auth import router as auth_router
from api.errors.http_error import http_error_handler
from api.errors.validation_error import http422_error_handler


import db

app = FastAPI(title="DBZ API",
    docs_url="/docs",
    version="0.0.1")

@app.get("/")
async def main(request: Request):
    return {
        'message': 'DBZ API'
    }


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.include_router(api_router.router)
app.include_router(auth_router.router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


