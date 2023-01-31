from flask import Flask, request, render_template, jsonify
import redis
import mysql.connector
from logging.handlers import RotatingFileHandler
from time import strftime
import logging
import traceback

app = Flask(__name__)

# Connect to Redis database
redis_db = redis.Redis(host="redis-db", port=6379)

# Connect to MySQL database
mysql_db = mysql.connector.connect(
    host="mysql-db",
    user="app",
    password="",
    database="test"
)

@app.route("/")
def index():
    # Increment the number of visits in Redis
    visits = redis_db.incr("visits")

    # Retrieve the latest messages from MySQL
    cursor = mysql_db.cursor()
    cursor.execute("SELECT message, id FROM messages ORDER BY id DESC LIMIT 10")
    messages = cursor.fetchall()
    data={'messages':messages,'visits':visits}

    return render_template('index.html', **data)
    

@app.route("/", methods=["POST"])
def add_message():
    # Retrieve the message from the form
    message = request.form["message"]

    # Store the message in the database
    cursor = mysql_db.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    mysql_db.commit()

    return "Message sent!"

@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%m-%d %H:%M]')
        logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    # tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path)
    return "Internal Server Error", 500

if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)        
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(debug=True,host='0.0.0.0', port='5000')
