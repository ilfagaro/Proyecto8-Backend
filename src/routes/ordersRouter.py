from flask import Blueprint

from src.services.OrdersService import OrdersService

main = Blueprint('orders_blueprint', __name__)

main = Blueprint('orders_blueprint', __name__)

@main.route('/')

def get_order(s):
    OrdersService().get_order()
    print('order se ve en consola')
    return 'order se ve en pagina'
