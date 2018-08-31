from flask import Flask
import sqlite3
import json

app = Flask(__name__)

@app.route('/hello')
def index():
    conn = sqlite3.connect('pcvdata.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pcv_matches')
    print (json.dumps(c.fetchall()))
    return json.dumps(c.fetchall())

if __name__ == '__main__':
    app.run()