import json
import time

from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel

app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers="127.0.0.1:9092",
    value_serializer=lambda v: json.dumps(v).encode(),
)
TOPIC = "iot"


class Payload(BaseModel):
    device_id: str
    metric: float
    unit: str


@app.post("/ingest")
async def ingest(p: Payload):
    event = {"ts": int(time.time() * 1000), **p.model_dump()}
    producer.send(TOPIC, event)
    return {"status": "ok"}
