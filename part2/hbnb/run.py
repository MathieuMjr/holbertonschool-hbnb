from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # ici, app.run prendra un objet de type config
    # import à faire : import config
    # on pourra alors faire app.run(config['development'])
    # par exemple, qui appellera une instance de la classe
    # configdevelopement via le dictionnaire config du
    # dossier config.py
