import redis
import values
from fetch_sql import FetchSql
from conversion import Conversion

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
        length = len(record)
        for i in range(0, len(record)):
            for j in range(len(record[i])):
                key = record[i][j]
                val = self.r.get(key)
                if val is None:
                    # raise ValueError("Key is NULL!")
                    fetch_key_table = values.fetch_key_table[values.transactiontable_id_list[0]]
                    fs = FetchSql(fetch_key_table)
                    row = Conversion.convert_to_byte(fs.value)
                    for value in row:
                        self.r.lpush(key, str(value))
                    # print(fs.value)
                else:
                    # check_value = self.r.get(key)
                    print("Key exist...")

        # key = record[0][0]

        check_value = self.r.get(key)
        if check_value is None:
            # Go through SQL server and fetch data of the KEY and insert it to the
            # corresponding key.
            fetch_key_table = values.fetch_key_table[values.transactiontable_id_list[0]]
            fs = FetchSql(fetch_key_table)
            print(fs.value)
            # self.r.set(key, "Mohsen")
