import sqlite3

from flask import Flask, render_template,request
from model import Transformer
#from sqlmodel import create_table, data_entry,close ,conn,
import sqlmodel
app = Flask(__name__)

users = [
    #first exemple
    {
        'name'     : 'akif',
        'surname'  : 'capoglu',
        "sentence" : 'insanlardan haz etmiyorum'
    }
]

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("database.sqlite")
    except sqlite3.error as e:
        print(e)

    return conn
@app.route("/", methods=["GET","POST"])
def to_database():
    #conn = db_connection()
    #cursor = conn.cursor()
    sqlmodel.create_table()
    # data_entry(new_user)

    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        global users#,c
        new_user = {
            'name'     : request.form['name'],
            'surname'  : request.form['surname'],
            "sentence" : request.form['sentence']
        }

        users.append(new_user)
        infos = list(filter(lambda x: x["name"] == request.form['name'], users))

        model  = Transformer()
        result = model.analyse(infos[0]["sentence"])
        return render_template('results.html',path="see", text =infos[0]["sentence"] ,data=result)


@app.route("/<string:name>", methods=['GET'])
def see(name):
    global users
    infos = list(filter(lambda x:x["name"] == name, users))
    if(len(infos)>0):
        return infos[0]
    return 404

@app.route("/see", methods=['GET'])
def see_all():
    if request.method == "GET":
        global users
        sqlmodel.close()
        #infos = list(filter(lambda x:x["name"] == name, users))
        #return render_template('results.html', data=len(users))
        return render_template('results.html', path="" ,data=dict(zip([f"{x}" for x in range(len(users))],users)))



if __name__ == '__main__':
    pass

