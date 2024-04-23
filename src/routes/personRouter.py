from flask import Blueprint, request
from src.models.personModel import Person
from src.services.PersonService import PersonService

main = Blueprint('person_blueprint', __name__)

# @main.route('/person/<DNI_Person>', methods=['GET', 'POST'])

# def manage_person():
#     if request.method == 'GET':
#         return get_person()
#     elif request.method == 'POST':
#         return post_person()
    
# @main.route('/person/post>', methods=['PUT', 'DELETE'])

# def mofiy_person(DNI_Person):
#     if request.method == 'PUT':
#         return update_person(DNI_Person)
#     elif request.method == 'DELETE':
#         return delete_person(DNI_Person)

@main.route('/person/<DNI_Person>', methods=['GET'])   
def get_person(DNI_Person):
    
    return PersonService.get_person(DNI_Person)
  #  print (get_person)
  #  return "metodo  get_person"

@main.route('/person', methods=['POST'])
def post_person():

    DNI_Person = request.json['DNI_Person']
    Name_Person = request.json['Name_Person']
    Email_Person = request.json['Email_Person']
    Adress_Person = request.json['Adress_Person']
    Telephone_Person = request.json['Telephone_Person']

    person = Person(DNI_Person, Name_Person, Email_Person, Adress_Person, Telephone_Person)
    post_person = PersonService.post_person(person)
    
    return PersonService.post_person(person)
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
