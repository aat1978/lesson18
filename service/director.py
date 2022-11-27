from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, dir_id):
        return self.dao.get_one(dir_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        dir_id = data.get("id")
        director = self.get_one(dir_id)

        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data):
        dir_id = data.get("id")
        director = self.get_one(dir_id)

        if "name" in data:
            director.name = data.get("name")

        self.dao.update(director)

    def delete(self, dir_id):
        self.dao.delete(dir_id)

