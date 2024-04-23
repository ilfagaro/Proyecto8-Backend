from src.database.dbmysql import get_connection
from src.models.userTypeModel import UserType

class UserTypeService():
    @classmethod
    def get_usertype(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usertype")
                result = cursor.fetchall()
                print(result)

            connection.close()
            return 'hola, este es el metodo get usertype imprimido en la página'

        except Exception as ex:

            print(ex)
    @classmethod
    def post_usertype(self, usertype: UserType):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_UserType = usertype.ID_UserType
                Name_UserType = usertype.Name_UserType

                cursor.execute("INSERT INTO usertype (ID_UserType, Name_UserType)"+
                                "VALUES ('{0}', '{1}');"
                                .format(ID_UserType, Name_UserType))

                connection.commit()

            connection.close()

            return 0

        except Exception as ex:

            print(ex)