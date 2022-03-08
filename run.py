import values
from kafka_work import KafkaWork

kw = KafkaWork(values.kafka_config)

kw.create_consumer()
kw.create_producer()
kw.add_message()
# print(type(kw.value))
print(50*'-')