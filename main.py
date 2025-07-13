from fastapi import FastAPI, Request
import uvicorn
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from api import router as api_router
from contextlib import asynccontextmanager
from auth import router as auth_router
from api.errors.http_error import http_error_handler
from api.errors.validation_error import http422_error_handler
from config.rabbitmq import rabbitmq_manager

# Define an async context manager for application lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event: Connect to RabbitMQ
    print("Connecting to RabbitMQ...")
    await rabbitmq_manager.connect()
    yield
    # Shutdown event: Disconnect from RabbitMQ
    await rabbitmq_manager.disconnect()

app = FastAPI(title="DBZ API",
    docs_url="/docs",
    version="0.0.1",
    lifespan=lifespan
    )


@app.get("/")
async def main(request: Request):
    return {
        'message': 'DBZ API'
    }

@app.get('/publish-notification')
async def publish_notification(request: Request):
    """Endpoint to publish a notification message to RabbitMQ."""
    messages = [
        "Goku has achieved a new transformation!",
        "Vegeta is training harder than ever!",
        "Frieza is plotting his next move!",
        "Bulma has invented a new gadget!",
        "Piccolo is meditating to enhance his powers!"
    ]
    for message in messages:
        await rabbitmq_manager.publish_message(message)
        print(f"Notification '{message}' published to RabbitMQ.")
    return {"status": "success", "message": "Notifications published successfully."}

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.include_router(api_router.router)
app.include_router(auth_router.router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


