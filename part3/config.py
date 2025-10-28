import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False


# hérite de config et surchage debut:
class DevelopmentConfig(Config):
    DEBUG = True


# dictionnaire ou les clé sont associées à un type de config
# dans run.py, on choisira le type de config souhaité
config = {"development": DevelopmentConfig, "default": DevelopmentConfig}
