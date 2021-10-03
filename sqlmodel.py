import sqlite3
import typing
conn = sqlite3.connect("database.sqlite")

c    = conn.cursor()

def create_table() -> None:
    sql_query = ("CREATE TABLE IF NOT EXISTS flashdata "+
                 "(username TEXT PRIMARY KEY ,"+
                "sersurname TEXT NOT NULL ,"+
                "sentence TEXT NOT NULL )")
    c.execute(sql_query)

def data_entry(user_dict : typing.Dict[str, str])-> None:
    print(user_dict)
    c.execute("INSERT INTO flashdata VALUES('{0}','{1}','{2}')".format(user_dict["name"], user_dict["surname"], user_dict["sentence"]))
    conn.commit()

def read_from_db()-> typing.List :
    """
    output : list of tuple which include 3 elements
    data[0] -> name
    data[1] -> surname
    data[2] -> sentence
    """
    c.execute("SELECT * FROM flashdata")
    data = c.fetchall()
    for i in data:
        print(i)
    return data

def close() -> None:
    c.close()
    conn.close()

"""
create_table()
data_entry(temp)
df = read_from_db()
close()
"""
