from kafka import KafkaProducer
from json import dumps
from time import sleep
from json import dumps

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
# Asynchronous by default
for e in range(1000):
    data = {'number' : e}
    future =  producer.send('text_topic', value=data)
    sleep(5)

record_metadata = future.get(timeout=10)


# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)