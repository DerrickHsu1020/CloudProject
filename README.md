This is the mini project for Cloud Computing:

A Flask app using air quality API that needs authentication!

The app.py includes a request for airquality in past three hours via breezometer.com

The API license will expire at 2nd of April, 2019



Description of API:

past3hours():
app.route('/airquality/<lat>/<lng>'),
parameters:<lat>, <lng>
lat should be between -90~90
lng should be between -180~180
This request returns and send the hourly historical air quality information at QueenMary for the past three hours to cassandra database.

airquality()::
This request returns


profile(name):
parameters:name

This request returns the HP for the pokemon(name)
