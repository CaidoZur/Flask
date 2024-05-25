from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "sakila"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM actor")
    actors = cur.fetchall()
    cur.close()
    return render_template("index.html", actors=actors)

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

@app.route("/actors/<int:id>", methods=["GET", "POST"])
def update_actor(id):
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM actor WHERE actor_id = %s", (id,))
        actor = cur.fetchone()
        cur.close()
        return render_template("update.html", actor=actor)
    elif request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s
        """, (first_name, last_name, id),
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["GET"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM actor where actor_id = %s """,(id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
