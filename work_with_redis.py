import redis
import values
from fetch_sql import FetchSql

class WorkRedis:
    def __init__(self, record=None):
        if record is None:
            self.record = None
        else:
            self.record = record
        self.r = self._initialize_redis()

    @staticmethod
    def _initialize_redis():
        r = redis.Redis("127.0.0.1", 6379)
        if r is None:
            raise ValueError("Redis server is not initialized!")
        else:
            return r

    def check_if_id_exists(self, record):
        key = record[0][0]
        check_value = self.r.get(key)
        if check_value is None:
            # Go through SQL server and fetch data of the KEY and insert it to the
            # corresponding key.
            fetch_key_table = values.fetch_key_table[values.transactiontable_id_list[0]]
            fs = FetchSql(fetch_key_table)
            self.r.set(key, "Mohsen")
