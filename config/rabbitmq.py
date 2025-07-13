# rabbitmq_utils.py
import asyncio
import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractChannel
from config.config import AMQP_URL, RABBITMQ_QUEUE

NOTIFICATIONS_QUEUE = "notifications_queue"

class RabbitMQManager:
    def __init__(self):
        self.connection: AbstractRobustConnection = None
        self.channel: AbstractChannel = None
        self.queue = None

    async def connect(self):
        """Establishes a robust connection to RabbitMQ."""
        try:
            self.connection = await aio_pika.connect_robust(AMQP_URL)
            self.channel = await self.connection.channel()
            self.queue = await self.channel.declare_queue(RABBITMQ_QUEUE, durable=True)
            print("Connected to RabbitMQ")
        except Exception as e:
            print(f"Failed to connect to RabbitMQ: {e}")
            # You might want to implement retry logic here

    async def disconnect(self):
        """Closes the RabbitMQ connection."""
        if self.channel:
            await self.channel.close()
            print("RabbitMQ channel closed.")
        if self.connection:
            await self.connection.close()
            print("RabbitMQ connection closed.")

    async def publish_message(self, message: str, routing_key: str = NOTIFICATIONS_QUEUE):
        """Publishes a message to the specified queue."""
        if not self.channel:
            print("RabbitMQ channel not available, attempting to reconnect...")
            await self.connect() # Reconnect if connection was lost (robust connection handles most cases)

        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key,
        )
        print(f"Published message: '{message}' to queue '{routing_key}'")

rabbitmq_manager = RabbitMQManager()