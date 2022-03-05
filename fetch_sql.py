from make_sql_connection import MakeSqlConnection
from sql_commands import SqlCommand


class FetchSql:
    # def __init__(self, table_name):
    #     self.conn = MakeSqlConnection(table_name=table_name)
    #     self.table_name = table_name
    #     self.value = self._fetch_data()

    def __init__(self, key_name, operation):
        self.conn = MakeSqlConnection()
        sc = SqlCommand(key_name)
        sc.return_command(operation)
        self.result = self._fetch_data(sc.commands)

    def _fetch_data(self, command):
        # command = SqlCommand()
        # command = "select top 10 * from " + self.table_name
        return self.conn.execution_command(command=command, command_type='select')


