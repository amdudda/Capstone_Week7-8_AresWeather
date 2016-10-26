'''
This imports data from the API and saves it to the database.
'''
from mysite.marsweather.models import Weather
from mysite.mysite import settings
import os


def setup():
    '''
    This sets up the database if there's no data in the system.
    :return: True if successful
    '''

    return True

if (__name__ == "__main__"):
    settings.configure()
    print(Weather.objects.all())