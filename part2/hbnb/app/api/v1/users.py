from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(
        required=True, description='First name of the user'),
    'last_name': fields.String(
        required=True, description='Last name of the user'),
    'email': fields.String(
        required=True, description='Email of the user')
    # ajouter un champs password à l'avenir
})


@api.route('/')
class UserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        # hasher le password ici

        # Simulate email uniqueness check
        # (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
            }, 201


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """This function retrieve of user
        by its id
        """
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }, 200


@api.route('/<user_id>')
class UserUpdate(Resource):
    @api.response(200, "OK")
    @api.response(404, "Not Found")
    @api.response(400, 'Bad Request')
    def put(self, user_id):
        """
        This method in charge of modifying user's
        informations
        """
        update_datas = api.payload
        user = facade.get_user(user_id)
        if not user:
            return {"error": "Not found"}, 404
        user_mail = facade.get_user_by_email(update_datas['email'])
        if user_mail and user_mail.id != user_id:
            return {"error": "Email already exist"}, 400
        facade.update(user_id, update_datas)
        return user.to_dict()


@api.route('/')
class UserList(Resource):
    @api.response(200, 'OK')
    def get(self):
        """
        This function responsible for
        fetching all users informations
        """
        users = facade.get_all()
        new_list = []
        for element in users:
            new_list.append(element.to_dict())
        return new_list
