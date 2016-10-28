'''
This takes data I gleaned from the API and saves it to the database.
see https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
for how to set this up.  I left out _private.py since I don't seem to need it.
'''
from ...models import Weather
from django.core.management.base import BaseCommand, CommandError
import requests  # documentation: http://docs.python-requests.org/en/master/user/quickstart/
import json as JSON

class Command(BaseCommand):
    help = 'Fetches archival data from MAAS website.'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # TODO: verify database is actually empty before pushing data to db... it's not accepting user input for some reason...
        del_and_import = 'n'
        OK_to_process_data = True
        '''
        if (Weather.objects.first()):
            del_and_import = input("There is already data in the database. OK to delete and reload (y for 'yes')?\n> ")
            print("proceed flag set to: " + del_and_import)
            if del_and_import.lower() == "y":
                # delete all records
                Weather.objects.all().delete()
            else:
                # tell the user the program's aborting the upload and set process_data to False so it doesn't
                # try to download any data
                print("You have chosen not to delete and reload data. Aborting data import.")
                OK_to_process_data = False
        # end check for existing data
        '''
        # TODO for now, let's just wipe everything and reload...
        print("Deleting and replacing database records.")
        if (Weather.objects.first()): Weather.objects.all().delete()
        if OK_to_process_data:
            '''
            to just load hardcoded sample data, before running:
            1. uncomment the load_sample_data line and
            2. comment out the load_api_data line.
            '''
            # self.load_sample_data()
            self.load_api_data()
        # end data upload
    # end handler

    def load_api_data(self):
        url = 'http://marsweather.ingenology.com/v1/archive/?format=json'
        next_page = True  # set to true to get us through first page of data...
        # counter used for debugging while loop
        counter = 0
        while next_page:  # and counter < 5:
            r = requests.get(url).json()
            next_page = r['next']
            weatherdata = r['results']
            for record in weatherdata:
                # grab our records and store them in a weather object
                w = Weather(
                    terrestrial_date=record['terrestrial_date'],
                    sol=record['sol'],
                    ls=record['ls'],
                    min_temp=record['min_temp'],
                    min_temp_fahrenheit=record['min_temp_fahrenheit'],
                    max_temp=record['max_temp'],
                    max_temp_fahrenheit=record['max_temp_fahrenheit'],
                    pressure=record['pressure'],
                    pressure_string=record['pressure_string'],
                    abs_humidity=record['abs_humidity'],
                    wind_speed=record['wind_speed'],
                    wind_direction=record['wind_direction'],
                    atmo_opacity=record['atmo_opacity'],
                    season=record['season'],
                    sunrise=record['sunrise'],
                    sunset=record['sunset']
                )
                # save the data to the database
                w.save()
            # end for record in weatherdata

            # debugging; and print out to confirm data has been saved correctly
            # print(Weather.objects.all());

            # set url to next page in data
            url = next_page
            counter += 1
            print("page " + str(counter) + " processed.")
            # end while loop

    # end load_api_data

    def load_sample_data(self):
        '''
        This loads sample data to the database.  Legacy use only.
        :return:
        '''
        devData = JSON.loads(
            '{"count": 29, "next": "http://marsweather.ingenology.com/v1/archive/?page=2&terrestrial_date_end=2012-10-31&terrestrial_date_start=2012-10-01&format=json", "previous": null, "results": [{"terrestrial_date": "2012-10-31", "sol": 84, "ls": 198.6, "min_temp": -70.0, "min_temp_fahrenheit": -94.0, "max_temp": -0.5, "max_temp_fahrenheit": 31.1, "pressure": 8.04, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-30", "sol": 83, "ls": 198.0, "min_temp": -72.5, "min_temp_fahrenheit": -98.5, "max_temp": -0.5, "max_temp_fahrenheit": 31.1, "pressure": 8.0051, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-29", "sol": 82, "ls": 197.4, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -0.4, "max_temp_fahrenheit": 31.28, "pressure": 7.98, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-28", "sol": 81, "ls": 196.8, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.5, "max_temp_fahrenheit": 29.3, "pressure": 7.99, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-27", "sol": 80, "ls": 195.6, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.97, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-26", "sol": 79, "ls": 195.0, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -2.0, "max_temp_fahrenheit": 28.4, "pressure": 7.955, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-25", "sol": 78, "ls": 194.5, "min_temp": -71.0, "min_temp_fahrenheit": -95.8, "max_temp": 0.0, "max_temp_fahrenheit": null, "pressure": 7.94, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-24", "sol": 77, "ls": 193.9, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.93, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-23", "sol": 76, "ls": 193.9, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.91, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}, {"terrestrial_date": "2012-10-22", "sol": 75, "ls": 193.0, "min_temp": -73.0, "min_temp_fahrenheit": -99.4, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 7.91, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 7", "sunrise": null, "sunset": null}]}')[
            'results'];
        for record in devData:
            # grab our records and store them in a weather object
            w = Weather(
                terrestrial_date=record['terrestrial_date'],
                sol=record['sol'],
                ls=record['ls'],
                min_temp=record['min_temp'],
                min_temp_fahrenheit=record['min_temp_fahrenheit'],
                max_temp=record['max_temp'],
                max_temp_fahrenheit=record['max_temp_fahrenheit'],
                pressure=record['pressure'],
                pressure_string=record['pressure_string'],
                abs_humidity=record['abs_humidity'],
                wind_speed=record['wind_speed'],
                wind_direction=record['wind_direction'],
                atmo_opacity=record['atmo_opacity'],
                season=record['season'],
                sunrise=record['sunrise'],
                sunset=record['sunset']
            )
            # save the data to the database
            w.save()
        # end for record in devData
        # debugging; and print out to confirm data has been saved correctly
        print(Weather.objects.all());
    # end load_sample_data