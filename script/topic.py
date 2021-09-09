from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='group5')

topic_list = []
# topic_list.append(NewTopic(name="group4_test", num_partitions=1, replication_factor=2))
topic_list.append(NewTopic(name="text-topic", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="audio-topic", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

