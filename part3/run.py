from app import create_app
from app.services import facade

app = create_app()


# create base admin
def create_default_admin():
    # Vérifie si l'admin existe déjà pour éviter les doublons
    admin_email = "admin@example.com"
    existing_admin = facade.get_user_by_email(admin_email)
    if not existing_admin:
        admin_data = {
            "first_name": "Default",
            "last_name": "Admin",
            "email": admin_email,
            "password": "admin",  # mot de passe de test
            "is_admin": True
        }
        facade.create_user(admin_data)
        print(f"Default admin created: {admin_email}")
    else:
        print("Default admin already exists")


if __name__ == '__main__':
    create_default_admin()
    app.run(debug=True)
    # ici, app.run prendra un objet de type config
    # import à faire : import config
    # on pourra alors faire app.run(config['development'])
    # par exemple, qui appellera une instance de la classe
    # configdevelopement via le dictionnaire config du
    # dossier config.py
