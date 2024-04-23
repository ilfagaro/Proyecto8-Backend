from flask import Blueprint, request
from src.models.personModel import Person
from src.services.PersonService import PersonService

main = Blueprint('person_blueprint', __name__)

# @main.route('/', methods=['GET', 'POST'])

# def manage_person():
#     if request.method == 'GET':
#         return get_person()
#     elif request.method == 'POST':
#         return post_person()
    
# #@main.route('/', methods=['PUT', 'DELETE'])

# def mofiy_person(DNI_Person):
#     if request.method == 'PUT':
#         return update_person(DNI_Person)
#     elif request.method == 'DELETE':
#         return delete_person(DNI_Person)

@main.route('/get', methods=['GET'])   
def get_person_data():

    # DNI_Person = "12345678A"
    get_person_data=PersonService.get_person()
    
    # get_person=PersonService.get_person(DNI_Person)
    print(get_person_data)    
    return 'Esto es del personRouter'

@main.route('/post', methods=['POST'])
def post_person():
    try:
        data = request.get_json

        DNI_Person = data['DNI_Person']
        Name_Person = data['Name_Person']
        Email_Person = data['Email_Person']
        Adress_Person = data['Adress_Person']
        Telephone_Person = data['Telephone_Person']

        person = Person(DNI_Person, Name_Person, Email_Person, Adress_Person, Telephone_Person)
        result = PersonService.post_person(person)

        return 'esto es post de person'
    
    except Exception as ex:
        print ("Error al procesar solicitud")
        return "Error al procesar la solicitud"
   # print(post_person)
   # return "Persona añadida"

@main.route('/person/<DNI_Person>', methods=['PUT'])
def update_person(DNI_Person):

    DNI_Person = request.json['DNI_Person']
    Name_Person = request.json['Name_Person']
    Email_Person = request.json['Email_Person']
    Adress_Person = request.json['Adress_Person']
    Telephone_Person = request.json['Telephone_Person']

    person = Person(DNI_Person, Name_Person, Email_Person, Adress_Person, Telephone_Person)

    update_person=PersonService.update_person(person)
    return PersonService.update_person(person)
   # print (update_person)
   # return 'Persona modificada'

@main.route('/person/<DNI_Person>', methods=['DELETE'])
def delete_person(DNI_Person):

    delete_person=PersonService.delete_person(DNI_Person)

    return PersonService.delete_person(DNI_Person)
  #  print (delete_person)

  #  return 'Persona eliminada'
