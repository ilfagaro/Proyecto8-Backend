# from src.database.dbmysql import get_connection
# from src.models.usersModel import User
# from src.services.UsersService import UsersService
# from werkzeug.security import generate_password_hash
# from flask import Flask
# import pymysql

# class AuthService():
# @classmethod
# def login_user(cls, user: User):
#     try:
#         connection = get_connection()

#         with connection.cursor() as cursor:

        
#             cursor.callproc('sp_get_user'(user.Name_User, user.Password_User))
#             row = cursor.fetchone()

#             if row:
#                 authenticated_user = User(row[0], row[1], row[2], row[3], row[4])

#         connection.close()
#         return authenticated_user

#     except Exception as ex:
#         print(ex)