import json

from flask import Flask
from flask import jsonify
from flask import request
from configparser import ConfigParser
import pyodbc # to connect to SQL Server Database


app = Flask(__name__)
config_object = ConfigParser()
config_object.read("config.ini")

app.config['CORS_HEADERS'] = 'Content-Type'

# connecting to the database
server = config_object['dbconfig']['server']
database = config_object['dbconfig']['database']
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()
print("---Connected to Database---")

@app.route("/get-lists", methods=["POST"])
def get_lists():
    if request.method == 'POST':
        select_lists = "SELECT * FROM [todolist].[dbo].[lists_tl]"
        count = cursor.execute(select_lists)
        records = cursor.fetchall()
        print(records)
        data = []
        for row in records:
            list_records = {
                "ID" : row[0], "ToDo":row[1]
            }
            data.append(list_records)
        return jsonify({"response": "Record Exist!", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)