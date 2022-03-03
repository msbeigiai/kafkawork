import redis


class WorkRedis:
    def __init__(self, record=None):
        if record is None:
            self.record = None
        else:
            self.record = record
        self.r = self._initialize_redis()

    @staticmethod
    def _initialize_redis():
        return redis.Redis("172.31.70.21", 6379)

    def check_if_id_exists(self, record):
        check_value = self.r.get(record[0])
        if check_value is None:
            self.r.set(str(check_value), "Mohsen")
