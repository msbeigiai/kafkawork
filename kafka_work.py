from kafka import KafkaConsumer, KafkaProducer
from json import loads
from work_with_redis import WorkRedis
import values

wr = WorkRedis()


class KafkaWork:
    def __init__(self, kafka_config):
        self.consumer = None
        self.producer = None
        self.kafka_config = kafka_config
        self.id_values = kafka_config["id_values"]
        self.value = []
        self.message = []
        self.records = []

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
            value_serializer=self.kafka_config["value_deserializer"]
        )
        if self.producer is None:
            raise ValueError(f"Producer is NULL!")
        else:
            print(f"{self.producer} is established.")

    def add_message(self, number_of_records=1):
        if self.consumer is None:
            raise ValueError("Consumer is NULL!")
        else:
            for message in self.consumer:
                if message is None:
                    raise ValueError("There is no message to show!")
                else:
                    self.value.append(loads(message.value))
                    # print(message.value)
                    # print(50*'-')
                    num = self._list_len()
                    print(num)
                    print(50*'-')
                    self._fetch_id(loads(message.value))
                    self._check(self.message, self.records)

    def _list_len(self):
        return len(self.value)

    def _fetch_id(self, msg):
        self.message = []
        dict_records = {}
        self.records = []
        for i in range(len(self.id_values)):
            # dict_records = {m: m for m in msg["payload"]["after"][self.id_values[i]]}
            # records.append(msg["payload"]["after"][self.id_values[i]])
            id_name = msg["payload"]["after"][self.id_values[i]]
            self.records.append(self.id_values[i])
            dict_records[id_name] = msg["payload"]["after"][self.id_values[i]]
        self.message.append(dict_records)

    def _check(self, record, column_name):
        wr.check_if_id_exists(record, column_name)




