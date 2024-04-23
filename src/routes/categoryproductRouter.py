from flask import Blueprint, request
from src.models.categoryproductModel import Categoryproduct
from src.services.CategoryproductService import CategoryproductService

main = Blueprint('categoryproduct_blueprint', __name__)

@main.route('/', methods=['GET', 'POST'])
def manage_categoryproduct():
   if request.method == 'GET':
      return get_categoryproduct()
   elif request.method == 'POST':
      return post_categoryproduct()

def get_categoryproduct():
   get_categoryproduct =CategoryproductService.get_categoryproduct()
   print('categoryproduct se ve en consola')
   return 'categoryproduct se ve en pagina'

def post_categoryproduct():
   ID_CategoryProduct = request.json['ID_CategoryProduct']
   Name_CategoryProduct = request.json['Name_CategoryProduct']

   categoryproduct = Categoryproduct(ID_CategoryProduct, Name_CategoryProduct)

   print(post_categoryproduct)

   return 'Persona añadida'