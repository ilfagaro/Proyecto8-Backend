from flask import Blueprint, request
from src.models.productModel import Product
from src.services.ProductService import ProductService

main = Blueprint('product_blueprint', __name__)

# @main.route('/', methods=['GET', 'POST'])
# def manage_product():
#     if request.method == 'GET':
#         return get_product()
#     elif request.method == 'POST':
#         return post_product()
    
# @main.route('/<int:ID_Product>', methods=['PUT', 'DELETE'])

# def mofiy_product(ID_Product):
#     if request.method == 'PUT':
#         return put_product(ID_Product)
#     elif request.method == 'DELETE':
#         return delete_product(ID_Product)

@main.route('/products', methods=['GET'])
def get_product():
    get_product=ProductService.get_product()
   # print (get_product)
    return (get_product), 200, {'Content-Type': 'application/json'}

@main.route('/products', methods=['POST'])
def post_product():

    Name_Product = request.json['Name_Product']
    Price_Product = request.json['Price_Product']
    Stock_Product = request.json['Stock_Product']
    ID_CategoryProduct_FK = request.json['ID_CategoryProduct_FK']

    product = Product(Name_Product, Price_Product, Stock_Product, ID_CategoryProduct_FK)

    post_product = ProductService.post_product(product)
   # print(post_product)
    return post_product(), 200, {'Content-Type': 'application/json'} 

@main.route('/products/<int:ID_Product>', methods=['PUT'])
def update_product(ID_Product):

    ID_Product = request.json['ID_Product']
    Name_Product = request.json['Name_Product']
    Price_Product = request.json['Price_Product']
    Stock_Product = request.json['Stock_Product']
    ID_CategoryProduct_FK = request.json['ID_CategoryProduct_FK']

    product = Product(ID_Product, Name_Product, Price_Product, Stock_Product, ID_CategoryProduct_FK)

    update_product=ProductService.update_product(product)
   # print (update_product)

    return update_product() , 200, {'Content-Type': 'application/json'} 


@main.route('/products/<int:ID_Product>', methods=['DELETE'])
def delete_product(ID_Product):

    delete_product=ProductService.delete_product(ID_Product)
   # print (delete_product)

    return delete_product(ID_Product)