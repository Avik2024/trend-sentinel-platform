import time
from faker import Faker
from kafka import KafkaProducer
import json

fake = Faker()
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {
        "user": fake.user_name(),
        "message": fake.sentence()
    }
    producer.send('raw-events', value=data)
    print(f"Produced: {data}")
    time.sleep(1)
