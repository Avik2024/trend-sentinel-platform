from kafka import KafkaConsumer, KafkaProducer
from textblob import TextBlob
import json

consumer = KafkaConsumer('raw-events',
                         bootstrap_servers='kafka:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    data = message.value
    sentiment = TextBlob(data['message']).sentiment.polarity
    data['sentiment'] = sentiment
    producer.send('processed-events', value=data)
    print(f"Processed: {data}")
