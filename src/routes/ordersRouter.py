from flask import Blueprint, request
from src.models.ordersModel import Orders
from src.services.OrdersService import OrdersService

main = Blueprint('orders_blueprint', __name__)

# @main.route('/', methods=['GET', 'POST'])

# def manage_orders():
#     if request.method == 'GET':
#         return get_orders()
#     elif request.method == 'POST':
#         return post_orders()
    
# @main.route('/<int:ID_Order>', methods=['PUT', 'DELETE'])  

# def mofiy_orders(ID_Order):
#     if request.method == 'PUT':
#         return post_orders(ID_Order)
#     elif request.method == 'DELETE':
#         return delete_orders(ID_Order)


@main.route('/orders', methods=['GET'])
def get_orders():

    get_orders=OrdersService.get_orders()
  #  print (get_orders)
    return get_orders()

@main.route('/orders', methods=['POST'])
def post_orders():

    ID_Order = request.json['ID_Order']
    Date_Order = request.json['Date_Order']
    State_Order = request.json['State_Order']
    ID_User_FK = request.json['ID_User_FK']
    ID_Product_FK = request.json['ID_Product_FK']

    orders = Orders(ID_Order, Date_Order, State_Order, ID_User_FK, ID_Product_FK)

    post_orders = OrdersService.post_orders(orders)
 #   print(post_orders)
    return post_orders()

@main.route('/orders/<int:ID_Order>', methods=['PUT'])
def update_orders(ID_Order):

    ID_Order = request.json['ID_Order']
    Date_Order = request.json['Date_Order']
    State_Order = request.json['State_Order']
    ID_User_FK = request.json['ID_User_FK']
    ID_Product_FK = request.json['ID_Product_FK']

    orders = Orders(ID_Order, Date_Order, State_Order, ID_User_FK, ID_Product_FK)

    update_orders=OrdersService.update_order(orders)
   # print (update_orders)

    return update_orders()

@main.route('/orders/<int:ID_Order>', methods=['DELETE'])
def delete_orders(ID_Order):

    delete_orders=OrdersService.delete_order(ID_Order)
 #   print (delete_orders)

    return delete_orders(ID_Order)
