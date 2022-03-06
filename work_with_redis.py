import redis
import values
from fetch_sql import FetchSql
from conversion import Conversion
from sql_commands import SqlCommand

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

    def check_if_id_exists(self, record, column):
        for i in range(len(record)):
            for key, val in record[i].items():
                redis_key = self.r.get(key)
                if redis_key is None and val is not '':
                    fs = FetchSql(key)
                    row = Conversion.convert_to_byte(fs.result)
                    for value in row:
                        self.r.set(key, str(value))
                elif val == '':
                    print("Value is NULL for adding to Redis!")
                else:
                    # check_value = self.r.get(key)
                    print("Key exist...")
