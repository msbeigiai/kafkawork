from make_sql_connection import MakeSqlConnection


class FetchSql:
    def __init__(self, table_name):
        self.conn = MakeSqlConnection(table_name=table_name)
        self.table_name = table_name
        self.value = self._fetch_data()

    def _fetch_data(self):
        command = "select top 10 * from " + self.table_name
        return self.conn.execution_command(command=command, command_type='select')
