A Flask app using air quality API that needs authentication!

The app.py includes different requests for airquality via breezometer.com

The API license will expire at 2nd of April, 2019



Description of API:

airchart():
app.route('/airqualitychart'),
This request returns the hourly historical air quality information at Queen Mary, University of London. Starting from March 15, 2019 at 07:00:00 UTC and ending on March 15, 2019 at 10:00:00 UTC.

past3hours():
app.route('/airqualityforpasthours'),
This request returns the hourly historical air quality information at Queen Mary, University of London for past three hours.

local():
app.route('/localairquality'),
This request returns the current air quality information for United Kingdom
