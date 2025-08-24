# IOT - Spark Structured Streaming

This project simulates a simple local architecture that collects events from an IOT device and process them using Spark Structured Streaming.

The data is stored as Delta Tables in a Bronze and Silver/Gold style layer containing raw and aggregated data respectively.

## Components

- [spark_app.py](spark_app.ipynb) - A Jupyter Notebook containing the main logic of data processing with a Spark Application
- [api_getaway.py](api_getaway.py) - A simple REST API that receives IOTs events through and HTTP endpoint
- [device_simulator.py](device_simulator.py) - A simples Python script that generates random events and send them to the Api Getaway
- [kafka_consumer.py](kafka_consumer.py) - A Python script that helps to see messages available in the Kafka topic

# Running the application

To run the application follow the steps below:

1. Start Kafka 
2. Start Api Getaway
3. Start Spark Application
4. Start device simulator

## Kafka - Redpanda Docker Version

```shell
docker run -d --name redpanda \
  -p 9092:9092 -p 9644:9644 \
  redpandadata/redpanda:latest \
  redpanda start --overprovisioned --smp 1 --memory 1G \
  --reserve-memory 0M --node-id 0 --check=false \
  --kafka-addr PLAINTEXT://0.0.0.0:9092 \
  --advertise-kafka-addr PLAINTEXT://127.0.0.1:9092
```

To print detailed info about the Kafka topic run:

```shell
docker exec -it redpanda rpk topic describe iot -p
```

## Api Getaway

Run the api with Uvicorn
```shell
uvicorn api_getaway:app --host 0.0.0.0 --port 8000
```