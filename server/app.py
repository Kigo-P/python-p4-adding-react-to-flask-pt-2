from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Movie


# instantiating Flask using app
app = Flask(__name__)
# configuring Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
app.json.compact = False

# instantiating flask using CORS
CORS(app)
# instantiating migrate with the app and db
migrate = Migrate(app, db)

db.init_app(app)

# creating a route to get all movies
@app.route("/movies", methods = ["GET"])
def movies():
    # querying the Movies to get all the movies
    movie = [movie.to_dict() for movie in Movie.query.all()]
    # creating a conditional statement to show all movies if the method used was GET
    if request.method == "GET":
        # creating and returning a response with all movies
        response = make_response(jsonify(movie), 200)
        return response
    else:
        # create an error message with the status code in it
        return make_response(jsonify({"text": "Method Not Allowed"}), 405)


if __name__ == "__main__":
    app.run(port=5555)
