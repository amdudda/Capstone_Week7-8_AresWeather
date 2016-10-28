'''
This takes data I gleaned from the API and saves it to the database.
see https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
for how to set this up.  I left out _private.py since I don't seem to need it.
'''
from ...models import Weather
from django.core.management.base import BaseCommand, CommandError
import json as JSON

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # TODO: verify database is actually empty before pushing data to db...
        devData = JSON.loads(
            '{"count": 29, "next": "http://marsweather.ingenology.com/v1/archive/?page=2&terrestrial_date_end=2012-10-31&terrestrial_date_start=2012-10-01&format=json", "previous": null, "results": [{"terrestrial_date": "2012-10-31", "sol": 84, "ls": 198.6, "min_temp": -70.0, "min_temp_fahrenheit": -94.0, "max_temp": -0.5, "max_temp_fahrenheit": 31.1, "pressure": 8.04, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-30", "sol": 83, "ls": 198.0, "min_temp": -72.5, "min_temp_fahrenheit": -98.5, "max_temp": -0.5, "max_temp_fahrenheit": 31.1, "pressure": 8.0051, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-29", "sol": 82, "ls": 197.4, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -0.4, "max_temp_fahrenheit": 31.28, "pressure": 7.98, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-28", "sol": 81, "ls": 196.8, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.5, "max_temp_fahrenheit": 29.3, "pressure": 7.99, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-27", "sol": 80, "ls": 195.6, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.97, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-26", "sol": 79, "ls": 195.0, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -2.0, "max_temp_fahrenheit": 28.4, "pressure": 7.955, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-25", "sol": 78, "ls": 194.5, "min_temp": -71.0, "min_temp_fahrenheit": -95.8, "max_temp": 0.0, "max_temp_fahrenheit": null, "pressure": 7.94, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-24", "sol": 77, "ls": 193.9, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.93, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-23", "sol": 76, "ls": 193.9, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.91, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-22", "sol": 75, "ls": 193.0, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.91, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}]}')['results'];
        for record in devData:
            # grab our records and store them in a weather object
            w = Weather(
                terrestrial_date = record['terrestrial_date'],
                sol = record['sol'],
                ls = record['ls'],
                min_temp = record['min_temp'],
                min_temp_fahrenheit = record['min_temp_fahrenheit'],
                max_temp = record['max_temp'],
                max_temp_fahrenheit = record['max_temp_fahrenheit'],
                pressure = record['pressure'],
                pressure_string = record['pressure_string'],
                abs_humidity = record['abs_humidity'],
                wind_speed = record['wind_speed'],
                wind_direction = record['wind_direction'],
                atmo_opacity = record['atmo_opacity'],
                season = record['season'],
                sunrise = record['sunrise'],
                sunset = record['sunset']
                )
            #save the data to the database
            w.save()
        # end for record in devData
        # debugging; and print out to confirm data has been saved correctly
        print(Weather.objects.all());