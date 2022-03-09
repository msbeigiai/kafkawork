from make_sql_connection import MakeSqlConnection
from sql_commands import SqlCommand


class FetchSql:

    def __init__(self, key_name):
        self.conn = MakeSqlConnection()
        sc = SqlCommand(key_name)
        sc.return_command()
        self.result = self._fetch_data(sc.commands)

    def _fetch_data(self, command):
        return self.conn.execution_command(command=command, command_type='select')


