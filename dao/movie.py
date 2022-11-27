from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()


