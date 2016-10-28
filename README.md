#Mars Weather Rover site

## Browse Curiosity rover weather data

## Features

* Download data from {MAAS} API
    * As of 2010.OCT.28, the dataset is about 738 records long (approx. 75 pages of data) and takes about 25 minutes to download and save over a generic cable internet connection.
    * To upload the data, open a terminal and navigate to the mysite directory of the project root.  Enter the command "python manage.py dbsetup" and allow it to run.
* Graphical navigation via a web browser.
    * Tested on Ubuntu 15 with Firefox.
    * Page forward and back sol by sol.
    * Go to a specific sol via /marsweather/sol/n, where n is the sol number.
        * Graceful handling of nonexistent sols and sols with no data.
    * Navigate to first and last records.
* The program uses Python 3 and Django 1.10.2 with a sqlite3 database.

## Known Issues

* No way to update existing data.
    * Need to code a dbupdate command that can be invoked similarly to dbsetup.
* Nonexistent sols should be identified as such rather than loaded with a generic "no data for this sol" page.

## Future Development

* Exploit the atmo_opacity data to change the image so it matches the weather conditions.
* Implement a thermometer to visualize temperature data
* Perhaps implement a windsock image to represent wind speed.
* Extend this into a web-based educational game in which players can explore Mars while pretending to be the Curiosity rover, gathering data and learning about [areology](https://en.wikipedia.org/wiki/Geology_of_Mars).