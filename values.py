from json import loads

topic_name = 'DebeziumTestServer.dbo.TestDb1Table1'
def value_deserializer(): lambda x: loads(x.decode('utf-8'))


kafka_config = {
    "topic_name": topic_name,
    "bootstrap_servers": ['172.31.70.21:9092'],
    "auto_offset_reset": 'earliest',
    "enable_auto_commit": True,
    "group_id": 'my-group',
    "value_deserializer": value_deserializer
}