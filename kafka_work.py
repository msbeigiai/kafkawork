from kafka import KafkaConsumer, KafkaProducer


class KafkaWork:
    def __init__(self, kafka_config):
        self.consumer = None
        self.producer = None
        self.kafka_config = kafka_config

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

    def show_messages(self, number_of_records=1):
        if self.consumer is None:
            raise ValueError("Consumer is NULL!")
        else:
            for message in self.consumer:
                print(message.value)


