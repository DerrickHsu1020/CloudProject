import json
from flask import Flask, request, jsonify
from cassandra.cluster import Cluster
import requests
from pprint import pprint



cluster = Cluster(['cassandra'])
session = cluster.connect()

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name","World")
    return('<h1>Hello, {}!</h1>'.format(name))

#pass the air quality record to the cassandra database
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
        pprint(air)
        return('<h1>Data has been upload.</h1>')
    else:
        print(resp.reason)

    categories = {categ["datetime"]:categ["indexes"]["baqi"]["aqi"] for categ in air["data"]}
    for i in categories:
        rows = session.execute( """INSERT INTO air.stats(datetime,aqi) values('{}',{}))""".format(i,categories[i]))

# output the air quality
@app.route('/airquality/data')
def airquality():
    row=session.execute("""SELECT * FROM air.stats""")
    for q in row:
        return('<h1>The airquality in the past three hours is {}.</h1>'.format(q.aqi))

# output the pokemon HP
@app.route('/pokemon/<name>' , methods=['GET'])
def profile(name):
    rows = session.execute( """Select * From pokemon.stats where name = '{}'""".format(name))
    for pokemon in rows:
        return('<h1>{} has {} hp</h1>'.format(name,pokemon.hp))
    return('<h1>That Pokemon does not exist!</h1>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
