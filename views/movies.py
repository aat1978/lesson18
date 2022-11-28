from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filter = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }

        all_movies = movie_service.get_all(filter)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return movie_schema.dump(movie), 200
        except Exception:
            return "", 404

    def put(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update(req_json)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, uid: int):
        movie_service.delete(uid)
        return "", 204
