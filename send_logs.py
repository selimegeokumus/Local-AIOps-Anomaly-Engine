import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Test logları gönderiyoruz
logs = [
    {"level": "INFO", "message": "User logged in successfully."},
    {"level": "INFO", "message": "Database query executed in 12ms."},
    {"level": "ERROR", "message": "PostgreSQL connection pool exhausted. Max connections: 100 reached!"}
]

for log in logs:
    producer.send('system-logs', log)
    print(f"Gönderildi: {log['level']}")
    time.sleep(2)

producer.flush()