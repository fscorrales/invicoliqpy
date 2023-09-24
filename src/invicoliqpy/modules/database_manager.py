from main import *

class DatabaseManager:
    def __init__(self, database_name):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(database_name)

    def open_connection(self):
        if self.db.open():
            return True
        else:
            print("Error al abrir la conexión a la base de datos.")
            return False

    def close_connection(self):
        self.db.close()

    def execute_query(self, query_string):
        query = QSqlQuery()
        if query.exec_(query_string):
            self.db.commit()
            return True
        else:
            print("Error al ejecutar la consulta:", query.lastError().text())
            return False

    def create_table(self, table_name, columns):
        query_string = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        return self.execute_query(query_string)

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f":{key}" for key in data.keys()])
        query_string = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        query = QSqlQuery()
        for key, value in data.items():
            query.bindValue(f":{key}", value)
        if query.exec_(query_string):
            self.db.commit()
            return True
        else:
            print("Error al insertar datos:", query.lastError().text())
            return False

    def select_data(self, table_name, conditions=None):
        query_string = f"SELECT * FROM {table_name}"
        if conditions:
            query_string += f" WHERE {conditions}"
        query = QSqlQuery()
        if query.exec_(query_string):
            result = []
            while query.next():
                row = {}
                for i in range(query.record().count()):
                    field_name = query.record().fieldName(i)
                    row[field_name] = query.value(i)
                result.append(row)
            return result
        else:
            print("Error al seleccionar datos:", query.lastError().text())
            return []

    def update_data(self, table_name, data, conditions):
        set_values = ', '.join([f"{key} = :{key}" for key in data.keys()])
        query_string = f"UPDATE {table_name} SET {set_values} WHERE {conditions}"
        query = QSqlQuery()
        for key, value in data.items():
            query.bindValue(f":{key}", value)
        if query.exec_(query_string):
            self.db.commit()
            return True
        else:
            print("Error al actualizar datos:", query.lastError().text())
            return False

    def delete_data(self, table_name, conditions):
        query_string = f"DELETE FROM {table_name} WHERE {conditions}"
        if self.execute_query(query_string):
            return True
        else:
            print("Error al eliminar datos:", query.lastError().text()) #self.db.lastError().text()
            return False
