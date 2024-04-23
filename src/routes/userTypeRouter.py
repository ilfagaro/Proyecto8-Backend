from flask import Blueprint, request
from src.models.userTypeModel import UserType
from src.services.UserTypeService import UserTypeService

main = Blueprint('userType_blueprint', __name__)

@main.route('/', methods=['GET', 'POST'])
def manage_usertype():
    if request.method == 'GET':
        return get_usertype()
    elif request.method == 'POST':
        return post_usertype()

def get_usertype():
    get_usertype =UserTypeService.get_usertype()
    print('userType se ve en consola')
    return 'userType se ve en pagina'

def post_usertype():
    ID_UserType = request.json['ID_UserType']
    Name_UserType = request.json['Name_UserType']

    usertype = UserType(ID_UserType, Name_UserType)

    print(post_usertype)

    return 'Persona añadida'
