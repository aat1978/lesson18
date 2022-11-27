from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db
from dao.model.movie import Movie
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


# функция
def create_data(application, database):
    with application.app_context():
        database.create_all()
    g1 = Genre(id=1, name="комедия")
    g2 = Genre(id=2, name="сериал")

    d1 = Director(id=1, name="Вася")
    d2 = Director(id=2, name="Петя")

    m1 = Movie(id=1,
               title="Список",
               description="Романтическая история о молодой паре, стремящейся стать идеальной. Красавица и умница Кэтрин составляет список «доработок» для своего бойфренда Алекса, чтобы избавить его от недостатков.",
               trailer="https://www.ivi.ru/watch/158987",
               year=2018,
               rating=7.1,
               genre_id=1,
               director_id=1)
    m2 = Movie(id=2,
               title="Пансион",
               description="Своенравные девушки поступают в закрытый исправительный пансион на отдаленном острове. Но система перевоспитания даёт сбой и приводит к обратному эффекту. ",
               trailer="https://www.ivi.ru/watch/pansion",
               year=2022,
               rating=6.5,
               genre_id=2,
               director_id=2)

    with database.session.begin(subtransactions=True):
        database.session.add_all([g1, g2])
        database.session.add_all([d1, d2])
        database.session.add_all([m1, m2])


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    create_data(app, db)
    app.run()
