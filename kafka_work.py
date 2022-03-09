import json
from kafka import KafkaConsumer, KafkaProducer
from json import loads
from work_with_redis import WorkRedis
from pymongo import MongoClient

wr = WorkRedis()

CONNECTION_STRING = "mongodb+srv://sa:testpassword@cluster0.0djau.mongodb.net/test"
client = MongoClient('localhost:27017')
collection = client.Enriched.enriched7

class KafkaWork:
    def __init__(self, kafka_config):
        self.consumer = None
        self.producer = None
        self.kafka_config = kafka_config
        self.id_values = kafka_config["id_values"]
        self.value = None
        self.message = None
        self.records = []
        self.list_count = []
        self.number_of_producer = 1

    def create_consumer(self):
        self.consumer = KafkaConsumer(
            self.kafka_config["topic_name"],
            bootstrap_servers=self.kafka_config["bootstrap_servers"],
            auto_offset_reset=self.kafka_config["auto_offset_reset"],
            enable_auto_commit=self.kafka_config["enable_auto_commit"],
            group_id=self.kafka_config["group_id"],
            value_deserializer=self.kafka_config["value_deserializer"]
        )

        if self.consumer is None:
            raise ValueError(f"Consumer is NULL!")
        else:
            print(f"{self.consumer} is established.")
            print(self.consumer.topics())

    def create_producer(self):
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_config["bootstrap_servers"],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        if self.producer is None:
            raise ValueError(f"Producer is NULL!")
        else:
            print(f"{self.producer} is established.")

    def add_message(self):
        if self.consumer is None:
            raise ValueError("Consumer is NULL!")
        else:

            for message in self.consumer:
                if message is None:
                    raise ValueError("There is no message to show!")
                else:
                    self.value = loads(message.value)
                    self.list_count.append(self.value)
                    num = self._list_len()
                    print(num)
                    print(50*'-')
                    self._fetch_id(self.value)
                    self._check(self.message, self.value)
                    self._send_producer()

    def _list_len(self):
        return len(self.list_count)

    def _fetch_id(self, msg):
        dict_records = {}
        self.records = []
        for i in range(len(self.id_values)):
            id_name = msg["payload"]["after"][self.id_values[i]]
            self.records.append(self.id_values[i])
            dict_records[self.records[i]] = msg["payload"]["after"][self.id_values[i]]
        self.message = dict_records

    def _check(self, record, row_record):
        wr.check_if_id_exists(record, row_record)

    def _send_producer(self):
        self.number_of_producer = 1
        if self.producer is None:
            raise ValueError('Producer is NULL!')
        else:
            data = wr.row_record
            self.producer.send("enriched_producer_header_01", value=data)
            print(f'Number of total producer sent: {self.number_of_producer}')
            print('Sent to producer!')
            self.number_of_producer = self.number_of_producer + 1




