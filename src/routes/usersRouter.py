from flask import Blueprint, request
from src.models.usersModel import User
from src.services.UsersService import UsersService

main = Blueprint('users_blueprint', __name__)

# @main.route('/users', methods=['GET', 'POST'])

# def manage_users():
#     if request.method == 'GET':
#         return get_users()
#     elif request.method == 'POST':
#         return post_users()

# @main.route('/users/<int:ID_User>', methods=['PUT', 'DELETE'])

# def mofiy_users(ID_User):
#     if request.method == 'PUT':
#         return update_users(ID_User)
#     elif request.method == 'DELETE':
#         return delete_users(ID_User)

@main.route('/get', methods=['GET'])
def get_users():

    get_users=UsersService.get_users()
    print (get_users)
    return 'Esto es del userRouter'

@main.route('/post', methods=['POST'])
def post_users():
    
    Name_User = request.json['Name_User']
    Password_User = request.json['Password_User']
    ID_UserType_FK = request.json['ID_UserType_FK']
    DNI_Person_FK = request.json['DNI_Person_FK']

    user = User(Name_User, Password_User, ID_UserType_FK, DNI_Person_FK)
    post_users = UsersService.post_user(user)

    # print(post_users)
    return post_users()


@main.route('/users/<int:ID_User>', methods=['PUT'])
def update_users(ID_User):

    ID_User = request.json['ID_User']
    Name_User = request.json['Name_User']
    Password_User = request.json['Password_User']
    ID_UserType_FK = request.json['ID_UserType_FK']
    DNI_Person_FK = request.json['DNI_Person_FK']

    user = User(ID_User, Name_User, Password_User, ID_UserType_FK, DNI_Person_FK)

    update_user=UsersService.update_user(user)
   # print (update_user)

    return update_users(ID_User)

@main.route('/users/<int:ID_User>', methods=['DELETE'])
def delete_users(ID_User):

    delete_user=UsersService.delete_user(ID_User)
   # print (delete_user)

    return delete_users(ID_User)
