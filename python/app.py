import sqlite3, requests, time, logging, random
from flask import Flask, request, render_template
import redis
import mysql.connector
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')
print(metrics)


# Connect to Redis database
redis_db = redis.Redis(host="redis-db", port=6379)

# Connect to MySQL database
mysql_db = mysql.connector.connect(
    host="mysql-db",
    user="app",
    password="",
    database="test"
)
cursor = mysql_db.cursor()


@app.route("/")
def index():
    # Increment the number of visits in Redis
    visits = redis_db.incr("visits")

    # Retrieve the latest messages from MySQL
#    cursor = mysql_db.cursor()
    cursor.execute("SELECT message, id FROM messages ORDER BY id DESC LIMIT 10")
    messages = cursor.fetchall()
    data={'messages':messages,'visits':visits}

    return render_template('index.html', **data)
    

@app.route("/", methods=["POST"])
def add_message():
    # Retrieve the message from the form
    message = request.form["message"]

    # Store the message in the database
    #cursor = mysql_db.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    mysql_db.commit()

    return "Message sent!"


metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
