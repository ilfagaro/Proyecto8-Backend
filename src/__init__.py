from flask import Flask;

from .routes.categoryproductRouter import main as categoryproduct_blueprint
from .routes.ordersRouter import main as orders_blueprint
from .routes.personRouter import main as person_blueprint
from .routes.productRouter import main as product_blueprint
from .routes.usersRouter import main as users_blueprint
# from .routes import usersRouter
from .routes.userTypeRouter import main as userType_blueprint

app = Flask(__name__)

def init_app(config):

    app.config.from_object(config)

    app.register_blueprint(categoryproduct_blueprint, url_prefix='/categoryproduct')
    app.register_blueprint(orders_blueprint, url_prefix='/orders')
    app.register_blueprint(person_blueprint, url_prefix='/person')
    app.register_blueprint(product_blueprint, url_prefix='/product')
    app.register_blueprint(users_blueprint, url_prefix='/users')
        # app.register_blueprint(usersRouter.main, url_prefix='/users')
    app.register_blueprint(userType_blueprint, url_prefix='/userType')



    # app.register_blueprint(categoryproductRouter.main, url_prefix='/categoryproduct')
   
    # app.register_blueprint(ordersRouter.main, url_prefix='/orders')

    # app.register_blueprint(personRouter.main, url_prefix='/person')

    # app.register_blueprint(productRouter.main, url_prefix='/product')

    # app.register_blueprint(usersRouter.main, url_prefix='/users')

    # app.register_blueprint(userTypeRouter.main, url_prefix='/usertype')

    return app

    

    
   