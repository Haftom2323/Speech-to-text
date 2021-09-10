from kafka import KafkaConsumer
#from pymongo import MongoClient
from json import loads

# To consume latest messages and auto-commit offsets

# consumer = KafkaConsumer('group4_test',
#                          group_id='my-group',
#                          bootstrap_servers=['b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092'], auto_offset_reset='earliest')
consumer = KafkaConsumer(
    'text_topic',
     bootstrap_servers=['b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092','b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))