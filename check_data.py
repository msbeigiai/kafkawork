class CheckData:
    def __init__(self):
        pass

    # if value is in redis fetch it from redis and add it to the existing record and send it via kafka

    def check_if_value_is_exist(self, value):
        temp_value = r.get(value_key)
