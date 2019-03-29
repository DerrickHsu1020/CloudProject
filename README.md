This is the mini project for Cloud Computing:

A Flask app using air quality API that needs authentication!

The app.py includes a request for airquality in past three hours via breezometer.com

The API license will expire at 2nd of April, 2019


Description of API:

hello():
@app.route('/'),
Print Hello World on the main page

past3hours():
@app.route('/airquality')
This request returns the hourly historical air quality information at Queen Mary in the past three hours in json format 

airquality():
@app.route('/airquality/data'),
This request connects the cassandra database for returning the hourly air quality stats on 29 of March which aqi is greater than 50

profile(name):
@app.route('/pokemon/<name>')
This request returns the pokemon HP according the input name
