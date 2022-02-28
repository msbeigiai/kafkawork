import unittest
from kafka_work import KafkaWork
import values

kw = KafkaWork(kafka_config=values.kafka_config)


class TestKafkaWork(unittest.TestCase):
    def test_has_kafka_config(self):
        self.assertEqual(kw.kafka_config["topic_name"], values.kafka_config["topic_name"])

    def test_has_kafka_consumer(self):
        kw.create_consumer()
        self.assertTrue(kw.consumer)





unittest.main()