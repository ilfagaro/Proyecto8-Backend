from src.database.dbmysql import get_connection

class UserTypeService():
    def get_all(self):
        try:
            connection=get_connection()
            print(connection)

        except Exception as ex:

            print(ex)