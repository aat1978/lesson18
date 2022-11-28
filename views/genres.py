from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = genre_service.get_one(uid)
            return genre_schema.dump(genre), 200
        except Exception:
            return "", 404

    def put(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        genre_service.update(req_json)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        genre_service.update_partial(req_json)
        return "", 204

    def delete(self, uid: int):
        genre_service.delete(uid)
        return "", 204
