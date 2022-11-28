from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db
from dao.model.movie import Movie
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


# функция
if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
