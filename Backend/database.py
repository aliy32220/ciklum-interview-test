import pyodbc
import jsonify


class Database:
    def __init__(self, logging, config):
        self.logging = logging
        self.config = config

    def connect(self):
        try:
            connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.config['dbconfig']['server']+';DATABASE='+self.config['dbconfig']['database']+';Trusted_Connection=yes;'
            conn = pyodbc.connect(connection_string)
            return conn
        except Exception as e:
            self.logging.error(e)
            return None

    def select_todos(self):
        conn = self.connect()
        if conn is not None:
            cursor = conn.cursor()
            try:
                select_lists = "SELECT * FROM [todolist].[dbo].[lists_tl]"
                count = cursor.execute(select_lists)
                records = cursor.fetchall()
                print(records)
                data = []
                for row in records:
                    list_records = {
                        "ID" : row[0], "ToDo": row[1]
                    }
                    data.append(list_records)
                return data
            except Exception as exep:
                print(exep)

    def insert_todos(self, todo):
        conn = self.connect()
        if conn is not None:
            cursor = conn.cursor()
            try:
                query  = f"INSERT INTO [todolist].[dbo].[lists_tl] VALUES ('"+todo+"')"
                print(query)
                cursor.execute(query)
                conn.commit()
            except Exception as exep:
                print(exep)




