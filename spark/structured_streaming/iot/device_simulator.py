import time, requests, random
URL = "http://127.0.0.1:8000/ingest"
DEVICE = "esp32-dev-01"

while True:
    payload = {"device_id": DEVICE, "metric": round(20 + random.random()*5, 2), "unit":"C"}
    resp = requests.post(URL, json=payload, timeout=5)
    print ('Response: ', resp)
    time.sleep(2)  # envia a cada 2s