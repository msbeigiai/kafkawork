from json import loads

topic_name = 'DebeziumTestServer.dbo.RETAILTRANSACTIONTABLE'
# topic_name = 'dbhistory.RETAILTRANSACTIONTABLE.DebeziumTestServer'


def value_deserializer(): lambda x: loads(x.decode('utf-8'))


transactiontable_id_list = ['TRANSACTIONID', 'STORE', 'TERMINAL', 'CHANNEL', 'DATAAREAID', 'PARTITION']

fetch_key_table = {
    "TRANSACTIONID": "GBG_RETAILPERIODICISCOUNTLOG"
}

kafka_config = {
    "topic_name": topic_name,
    "bootstrap_servers": ['172.31.70.21:9092'],
    "auto_offset_reset": 'earliest',
    "enable_auto_commit": True,
    "group_id": 'some_group01',
    "value_deserializer": value_deserializer(),
    "id_values": transactiontable_id_list
}

database_config = {
    "database_name": "MicrosoftDynamicsNX",
    "table_name": "dbo.RETAILTRANSACTIONTABLE",
    "username": "sa",
    "password": "testpassword",
    "server": "tcp:172.31.70.20,1433"
}

