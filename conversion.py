from json import loads
import pyodbc


class Conversion:
    # def __init__(self):

    @staticmethod
    def convert_to_byte(row) -> list:
        row_as_list = [x for x in row]
        return row_as_list
