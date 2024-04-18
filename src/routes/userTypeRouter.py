from flask import Blueprint

from src.services.UserTypeService import UserTypeService
main = Blueprint('userType_blueprint', __name__)

@main.route('/')

def get_userType():
    UserTypeService().get_userType()    
    print('userType se ve en consola')
    return 'userType se ve en pagina'
