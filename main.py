from fastapi import FastAPI, Request
import uvicorn
from api import router as api_router


import db

app = FastAPI(title="Test Fast API",
    docs_url="/docs",
    version="0.0.1")

@app.get("/")
async def main(request: Request):
    return {
        'message': 'Hello World API'
    }

app.include_router(api_router.router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


