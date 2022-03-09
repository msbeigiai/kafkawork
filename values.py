import json
from json import loads

topic_name = 'DebeziumTestServer.dbo.RETAILTRANSACTIONTABLE'

def value_deserializer(): lambda x: loads(x.decode('utf-8'))
def value_serializer(): lambda x: json.dumps(x).encode('utf-8')


transactiontable_id_list = ['STORE', 'CUSTACCOUNT']
# " dbo.GBG_RETAILPERIODICISCOUNTLOG "

fetch_key_table = {
    "TRANSACTIONID": "RETAILTRANSACTIONTABLE"
}

kafka_config = {
    "topic_name": topic_name,
    "bootstrap_servers": ['172.31.70.21:9092'],
    "auto_offset_reset": 'earliest',
    "enable_auto_commit": True,
    "group_id": 'some_group01',
    "value_deserializer": value_deserializer(),
    "value_serializer": value_serializer(),
    "id_values": transactiontable_id_list
}

database_config = {
    "database_name": "MicrosoftDynamicsAX",
    "table_name": "dbo.RETAILTRANSACTIONTABLE",
    "username": "sa",
    "password": "testpassword",
    "server": "tcp:172.31.70.20,1433"
}

