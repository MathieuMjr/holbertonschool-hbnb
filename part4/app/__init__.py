from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.extensions import bcrypt
from app.extensions import jwt
from app.extensions import db
from flask_cors import CORS


def create_app(config_class="config.DevelopmentConfig"):
    # la string de config_class sera comprise comme un import
    # d'un objt de type developmentconfig depuis le fichier config
    # ici on ne fait que définir la fonction ; c'est dans run.py
    # qu'on l'appelera et qu'on indiquera quelle config lancer
    app = Flask(__name__)  # créer l'app
    app.config.from_object(config_class)  # charge la config
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # le r"/*" est un regex qui selectionne toutes les endpoint/route
    # puis dit que toutes les origines externes sont acceptées pour faire de requêtes
    # (à changer en prod)

    # config est un attribut de app :
    # un dictionnaire qui contient qui contient des clé
    # genre debug, etc. auxquelles on transmet les valeurs
    # via nos classes de config qui seront accessibles par
    # toutes les extension
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
    api.add_namespace(auth_ns, path='/api/v1/auth')

    return app
