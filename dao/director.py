from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, dir_id):
        return self.session.query(Director).get(dir_id)

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self, dir_id):
        director = self.get_one(dir_id)
        self.session.delete(director)
        self.session.commit()


