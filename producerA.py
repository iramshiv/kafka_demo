import time
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))
for even in range(100000):
    if even % 2 == 0:
        data = {'A': even}
        producer.send('numtest1', data)
        time.sleep(1)
producer.flush()