class Conversion:
    @staticmethod
    def convert_to_byte(row) -> list:
        row_as_list = [x for x in row]
        return row_as_list

    @staticmethod
    def convert_from_byte(byte_value) -> str:
        return byte_value.decode('utf-8')


