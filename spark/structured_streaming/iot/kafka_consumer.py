# consume_iot_from_beginning.py
import json, signal, sys, time
from kafka import KafkaConsumer, TopicPartition

TOPIC = "iot"
BOOTSTRAP = "127.0.0.1:9092"   # if using Redpanda Docker often it's 127.0.0.1:19092
GROUP_ID = None                # no group => no committed offsets

def main():
    # Create consumer without group so we can seek manually
    c = KafkaConsumer(
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="earliest",      # used for partitions we haven't positioned
        enable_auto_commit=False,
        value_deserializer=lambda b: json.loads(b.decode("utf-8")),
        key_deserializer=lambda b: b.decode() if b else None,
    )

    # Assign partitions explicitly and seek to beginning
    c.subscribe([TOPIC])
    while not c.assignment():
        c.poll(100)  # trigger assignment

    for tp in c.assignment():
        c.seek_to_beginning(tp)

    print(f"Reading ALL existing messages from '{TOPIC}' on {BOOTSTRAP} ...")
    try:
        while True:
            records = c.poll(timeout_ms=1000)
            if not records:
                # no more data at the moment; wait for new ones
                time.sleep(0.2)
                continue
            for tp, msgs in records.items():
                for m in msgs:
                    print(f"{tp.topic} p{tp.partition} off={m.offset} -> {m.value}")
    except KeyboardInterrupt:
        pass
    finally:
        c.close()

if __name__ == "__main__":
    main()