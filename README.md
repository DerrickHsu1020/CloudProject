This is the mini project for Cloud Computing:

A Flask app using air quality API that needs authentication!

The app.py includes a request for airquality in past three hours via breezometer.com

The API license will expire at 2nd of April, 2019



Description of API:

past3hours():
app.route('/airquality/')
This request returns and send the hourly historical air quality information at QueenMary for the past three hours and send the information to the cassandra database.

airquality():
app.route('/airquality/data')
This request returns the information from the cassandra database. Before execute this app, it needs to execute past3hours() first for insert data into the database if there is no data in the database.


profile(name):
parameters: name

This request returns the HP for the pokemon(name)
