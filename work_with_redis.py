import redis
import values
from fetch_sql import FetchSql
from conversion import Conversion


class WorkRedis:
    def __init__(self, record=None):
        self.row_record = None
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

    def check_if_id_exists(self, record, row_record):
        # for i in range(len(record)):
        self.row_record = None
        for key, val in record.items():
            redis_value = self.r.get(key+':'+val)
            if redis_value is not None:
                converted_value = Conversion.convert_from_byte(redis_value)
                print("Key exist...")
                row_record["payload"]["after"][key] = converted_value
                # self.row_record.append(row_record["payload"]["after"])
            elif redis_value is None and val is not '':
                fs = FetchSql(key)
                row = Conversion.convert_to_byte(fs.result)
                if row:
                    for value in row:
                        self.r.set(key+':'+val, str(value))
                        row_record["payload"]["after"][key] = value
                        # self.row_record.append(row_record["payload"]["after"])
                else:
                    row_record["payload"]["after"][key] = 'Empty Value: ' + val
            elif val == '':
                print("Value is NULL for adding to Redis!")

        self.row_record = row_record["payload"]["after"]
