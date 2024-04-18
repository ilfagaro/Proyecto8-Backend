from flask import Blueprint

from src.services.CategotyproductService import CategotyproductService

main = Blueprint('categoryproduct_blueprint', __name__)

@main.route('/')

def get_categoryproduct():
   CategotyproductService().get_categoryproduct()
   print('categoria de producto se ve en consola')
   return 'categoria de producto se ve en pagina'
