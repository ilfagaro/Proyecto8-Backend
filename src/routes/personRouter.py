from flask import Blueprint

from src.services.PersonService import PersonService

main = Blueprint('person_blueprint', __name__)

@main.route('/')

def get_person():
    PersonService().get_person()
    print('person se ve en consola')
    return 'person de producto se ve en pagina'
