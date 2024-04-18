from flask import Blueprint

from src.services.UsersService import UsersService

main = Blueprint('users_blueprint', __name__)

@main.route('/')

def get_users():
    UsersService().get_users()
    print('user se ve en consola')
    return 'user se ve en pagina'
