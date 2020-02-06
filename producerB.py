import time
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
for odd in range(100000):
    if odd % 2 != 0:
        data = {'B': odd}
        producer.send('numtest1', value=data)
        time.sleep(2)
producer.flush()
