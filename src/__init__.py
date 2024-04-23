from flask import Flask;

from .routes import categoryproductRouter
from .routes import ordersRouter
from .routes import personRouter
from .routes import productRouter
from .routes import usersRouter
from .routes import userTypeRouter

app = Flask(__name__)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(categoryproductRouter.main, url_prefix='/categoryproduct')
   
    app.register_blueprint(ordersRouter.main, url_prefix='/orders')

    app.register_blueprint(personRouter.main, url_prefix='/person')

    app.register_blueprint(productRouter.main, url_prefix='/product')

    app.register_blueprint(usersRouter.main, url_prefix='/users')

    app.register_blueprint(userTypeRouter.main, url_prefix='/usertype')

    return app

    

    
   