import json
from flask import Flask, request
from cassandra.cluster import Cluster
import requests

cluster = Cluster(['cassandra'])
session = cluster.connect()

app = Flask(__name__)

#Print Hello World on the main page
@app.route('/')
def hello():
    name = request.args.get("name","World")
    return('<h1>Hello, {}!</h1>'.format(name))

#Return the air quality in the past three hours in json format
@app.route('/airquality' , methods=['GET'])
def past3hours():
    airhours_url_template = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={lat}&lon={lng}&key={API_KEY}&hours=3'
    MY_API_KEY ='4b69b672b50e4775b672abcd5004c291'
    my_latitude = request.args.get('lat' , '51.52369')
    my_longitude = request.args.get('lng', '-0.0395857')
    air_hours_url = airhours_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=MY_API_KEY)
    resp = requests.get(air_hours_url)
    if resp.ok:
        air=resp.json()
        return('<h1>{}</h1>'.format(air))
    else:
        print(resp.reason)

#Connect the cassandra database for returning the hourly air quality stats on 29 of March which aqi is greater than 50
@app.route('/airquality/data')
def airquality():
    row=session.execute("""SELECT * FROM air.stats WHERE aqi>=50 ALLOW FILTERING""")
    for q in row:
        return('<h1>The hourly airquality at Queen Mary on 29 of March which aqi is greater than 50 is {}, {}.</h1>'.format(q.datetime,q.aqi))

#Return the pokemon HP according the input name
@app.route('/pokemon/<name>' , methods=['GET'])
def profile(name):
    rows = session.execute( """Select * From pokemon.stats where name = '{}'""".format(name))
    for pokemon in rows:
        return('<h1>{} has {} hp</h1>'.format(name,pokemon.hp))
    return('<h1>That Pokemon does not exist!</h1>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
