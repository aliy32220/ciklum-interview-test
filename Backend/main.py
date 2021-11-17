import json
import logging
import jsonify 
import request
from flask import Flask, Response, request
from configparser import ConfigParser
from database import Database


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(filename='logs.log',
                    level=logging.DEBUG,
                    format='%(levelname)s: %(message)s on %(asctime)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

config = ConfigParser()
config.read("config.ini")

@app.route("/get-lists", methods=["POST"])
def get_lists():
    # if request.method == 'POST':
        records = database.select_todos()
        print(records)
        return {"response": "Record Exist!", "data": json.dumps(records)}, 200

@app.route("/insert-lists", methods=["POST"])
def insert_lists():
    # if request.method == 'POST':
        data = json.loads(request.data)
        todo = data['todo']
        database.insert_todos(todo)
        return {"response": "Record Inserted!"}, 200

database = Database(logging, config)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)