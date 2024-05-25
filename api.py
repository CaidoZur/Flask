from flask import Flask, jsonify, make_response, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "sakila"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def intro():
    return '''
    <p>Welcome! Project by Zuriel Montallana!<p> 
    <p><a href="/actors">View Actors</a></p>
    '''

@app.route("/actors")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM actor")
    actors = cur.fetchall()
    cur.close()
    return render_template("index.html", actors=actors)

@app.route("/actors/<int:id>", methods=["GET"])
def get_actor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM actor WHERE actor_id = %s", (id,))
    actor = cur.fetchone()
    cur.close()

    if actor:
        return f"The actor with ID {id} is {actor['first_name']} {actor['last_name']}"
    else:
        return "Actor not found"

@app.route("/add", methods=["POST"])
def add_actor():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        cur = mysql.connection.cursor()
        cur.execute(
                """ INSERT INTO actor (first_name, last_name) VALUES (%s, %s)""", (first_name, last_name),
        )
        mysql.connection.commit()
        cur.close()
    return redirect(url_for("index"))

@app.route("/actors/<int:id>", methods=["GET", "PUT"])
def update_actor(id):
    if request.method == "PUT":
        cur = mysql.connection.cursor()
        info = request.get_json()
        first_name = info["first_name"]
        last_name = info["last_name"]
        cur.execute("""
            UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s
        """, (first_name, last_name, id),
        )
        mysql.connection.commit()
        rows_affected = cur.rowcount
        cur.close()
        return make_response(jsonify({"message": "UPDATED SUCCESSFULLY", "rows_affected": rows_affected}), 200)
    elif request.method == "GET":
        return "GET request for actor with ID: {}".format(id)

@app.route("/actors/<int:id>", methods=["GET", "DELETE"])
def delete_actor(id):
    if request.method == "DELETE":
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM actor WHERE actor_id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": f"Actor with ID {id} deleted successfully"})
    else:
        # If it's a GET request, you can return information about the actor
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM actor WHERE actor_id = %s", (id,))
        actor = cur.fetchone()
        cur.close()

        if actor:
            return f"The actor with ID {id} is {actor['first_name']} {actor['last_name']}"
        else:
            return "Actor not found"


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form["search_term"]
        query = """
            SELECT * FROM actor WHERE first_name LIKE %s OR last_name LIKE %s
        """
        like_term = f"%{search_term}%"
        cur = mysql.connection.cursor()
        cur.execute(query, (like_term, like_term))
        actors = cur.fetchall()
        cur.close()
        return render_template("index.html", actors=actors)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
