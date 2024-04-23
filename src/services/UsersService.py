from src.database.dbmysql import get_connection
from src.models.usersModel import User
from werkzeug.security import generate_password_hash
from flask import Flask
import pymysql

class UsersService():

    @classmethod
    def get_users(cls):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                result = cursor.fetchall()
                print(result)
                           
            connection.close()
            return 'hola, este es el metodo get USER imprimido en la página'

        except Exception as ex:

            print(ex)
    @classmethod
    def post_user(cls,users: User):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_User = users.ID_User
                Name_User = users.Name_User
                Password_User = users.Password_User
                ID_UserType_FK = users.ID_UserType_FK
                DNI_Person_FK = users.DNI_Person_FK

            

                cursor.execute("INSERT INTO users (ID_User, Name_User, Password_User, ID_UserType_FK, DNI_Person_FK)"+
                                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');"
                                .format(ID_User, Name_User, Password_User, ID_UserType_FK, DNI_Person_FK))

                connection.commit()
                                  
            connection.close()

            return 0    

        except Exception as ex:

            print(ex)
    @classmethod
    def update_user(cls,users: User):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:
                ID_User = users.ID_User
                Name_User = users.Name_User
                Password_User = users.Password_User
                ID_UserType_FK = users.ID_UserType_FK
                DNI_Person_FK = users.DNI_Person_FK

                cursor.execute("UPDATE users SET Name_User = '{0}', Password_User = '{1}', ID_UserType_FK = '{2}', DNI_Person_FK = '{3}' WHERE ID_User = '{4}';"
                                .format(Name_User, Password_User, ID_UserType_FK, DNI_Person_FK, ID_User))

                connection.commit()
                                  
            connection.close()

            return 0    

        except Exception as ex:

            print(ex)
    @classmethod
    def delete_user(cls,users: User):
        try:
            connection=get_connection()
            print(connection)

            with connection.cursor() as cursor:

                ID_User = users.ID_User

                cursor.execute("DELETE FROM users WHERE ID_User = '{0}';"
                                .format(ID_User))

                connection.commit()
                                  
            connection.close()

            return 0    

        except Exception as ex:

            print(ex)