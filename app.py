from flask import Flask, render_template

import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.missionToMars

db.team.drop()
@app.route('/')
def index():
    teams = list(db.team.find())
    print(teams)

    return render_template('index.html', teams=teams)


if __name__ == "__main__":
    app.run(debug=True)
