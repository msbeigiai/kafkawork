from kafka import KafkaConsumer, KafkaProducer
from json import loads

class KafkaWork:
    def __init__(self, kafka_config):
        self.consumer = None
        self.producer = None
        self.kafka_config = kafka_config
        self.id_values = kafka_config["id_values"]
        self.value = []
        self.message = None

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
                    # self.message = message
                    print(message.value)
                    # return message.value
                    print(50*'-')
                    num = self._list_len()
                    print(num)
                    print(50*'-')
                    self._fetch_id(num)

    def _list_len(self):
        return len(self.value)

    def _fetch_id(self, len_list):
        output = []
        records = []
        iterator = 0
        for i in range(len_list):
            val = self.value[i]
            while iterator < len(self.id_values):
                records.append(val["payload"]["after"][self.id_values[iterator]])
                iterator += 1

        for i in range(len_list):
            output.append(records)

        print(output)




