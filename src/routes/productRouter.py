from flask import Blueprint

from src.services.ProductService import ProductService

main = Blueprint('product_blueprint', __name__)

@main.route('/')

def get_product():
    ProductService().get_product()
    print('producto se ve en consola')
    return 'producto se ve en pagina'
