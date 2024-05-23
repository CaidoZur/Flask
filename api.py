from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "sakila"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/actors", methods=["GET"])
def get_actors():
    data = data_fetch("""select * from actor""")
    return make_response(jsonify(data), 200)

@app.route("/actors/<int:id>", methods=["GET"])
def get_actor_by_id(id):
    data = data_fetch("""SELECT * FROM actor where actor_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/actors/<int:id>/movies", methods=["GET"])
def get_movies_by_actor(id):
    data = data_fetch("""
    SELECT film.title, film.release_year
    FROM actor
    INNER JOIN film_actor
    ON actor.actor_id = film_actor.actor_id
    INNER JOIN film
    ON film_actor.film_id = film.film_id
    WHERE actor.actor_id = 2
    """.format(id))
    return make_response(jsonify({"actor_id":id, "count": len(data), "movies": data}), 200)

if __name__ == "__main__":
    app.run(debug=True)

