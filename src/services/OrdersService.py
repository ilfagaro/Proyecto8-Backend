from src.database.dbmysql import get_connection

class OrdersService():
    def get_all(self):
        try:
            connection=get_connection()
            print(connection)

        except Exception as ex:

            print(ex)