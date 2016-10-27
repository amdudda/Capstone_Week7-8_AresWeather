'''
This imports data from the API and saves it to the database.
'''
from mysite.marsweather.models import Weather


def setup():
    '''
    This sets up the database if there's no data in the system.
    :return: True if successful
    '''

    print(Weather.objects.all())
    return True

# if (__name__ == "__main__"):
print(Weather.objects.all())