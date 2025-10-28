from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from flask_jwt_extended import JWTManager


def create_app(config_class="config.DevelopmentConfig"):
    # la string de config_class sera comprise comme un import
    # d'un objt de type developmentconfig depuis le fichier config
    # ici on ne fait que définir la fonction ; c'est dans run.py
    # qu'on l'appelera et qu'on indiquera quelle config lancer
    app = Flask(__name__)
    app.config.from_object(config_class)
    # config est un attribut de app :
    # un dictionnaire qui contient qui contient des clé
    # genre debug, etc. auxquelles on transmet les valeurs
    # via nos classes de config qui seront accessibles par
    # toutes les extension
    jwt = JWTManager(app)

    api = Api(
        app, version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
        )

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
