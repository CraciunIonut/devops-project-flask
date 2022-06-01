from flask import request, Blueprint, render_template
import sqlite3

blueprintPut = Blueprint('putMethod', __name__)

@blueprintPost.route('/', methods=['PUT', 'GET'])
def query_record():
    if request.method == "GET":
        return render_template("putform.html")
        
    connection = sqlite3.connect("db/users.db")
    cursor = connection.cursor()
    _id = request.form('id')
    _name = request.form('name')

    query = "Update Users set name = '{}' where id = {}".format(_name,int(_id))

    cursor.execute(query)
    connection.commit()
    connection.close()

    return "Succesful"
