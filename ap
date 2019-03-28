from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import csv
import requests
from flask import Flask, request
#from cassandra.cluster import Cluster
from pprint import pprint
import requests_cache

requests_cache.install_cache('air_api_cache' , backend='sqlite' , expire_after=36000)


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

air_url_template = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={lat}&lon={lng}&key={API_KEY}&start_datetime={start}&end_datetime={end}'
MY_API_KEY = '4b69b672b50e4775b672abcd5004c291'
@app.route('/airqualitychart' , methods=['GET'])
def airchart():
    my_latitude = request.args.get('lat' , '51.52369')
    my_longitude = request.args.get('lng', '-0.0395857')
    my_start = request.args.get('start', '2019-03-15T07:00:00Z')
    my_end = request.args.get('end', '2019-03-15T10:00:00Z')
    air_url = air_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=MY_API_KEY, start=my_start, end=my_end)
    resp = requests.get(air_url)
    if resp.ok:
        resp = requests.get(air_url)
        pprint(resp.json())
    else:
        print(resp.reason)
    return ("Done!")

airhours_url_template = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={lat}&lon={lng}&key={API_KEY}&hours=3'
@app.route('/airqualityforpasthours' , methods=['GET'])
def past3hours():
    my_latitude = request.args.get('lat' , '51.52369')
    my_longitude = request.args.get('lng', '-0.0395857')
    air_hours_url = airhours_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=MY_API_KEY)
    resp = requests.get(air_hours_url)
    if resp.ok:
        resp = requests.get(air_hours_url)
        pprint(resp.json())
    else:
        print(resp.reason)
    return ("Done!")


airlocal_url_template = 'https://api.breezometer.com/air-quality/v2/current-conditions?lat={lat}&lon={lng}&key={API_KEY}&features=local_aqi'
@app.route('/localairquality' , methods=['GET'])
def local():
    my_latitude = request.args.get('lat' , '51.52369')
    my_longitude = request.args.get('lng', '-0.0395857')
    air_local_url = airlocal_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=MY_API_KEY)
    resp = requests.get(air_local_url)
    if resp.ok:
        resp = requests.get(air_local_url)
        pprint(resp.json())
    else:
        print(resp.reason)
    return ("Done!")



#cluster = Cluster(['cassandra'])
#session = cluster.connect()
@app.route('/pokemon/<name>' , methods=['GET'])
def profile(name):
    rows = session.execute( """Select * From pokemon.stats where name = '{}'""".format(name))
    for pokemon in rows:
        return('<h1>{} has {} attack!</h1>'.format(name,pokemon.attack))
    return('<h1>That Pokemon does not exist!</h1>')

if __name__=="__main__":
    app.run(port=8080, debug=True)
