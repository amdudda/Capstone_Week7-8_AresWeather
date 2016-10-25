from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Weather(models.Model):
    '''
    A model for our mars weather data.  Sample data noted in comments.
    '''
    # First element in tuple arguments is the verbose field name.
    #  https://docs.djangoproject.com/en/1.10/topics/db/models/#verbose-field-names
    terrestrial_date = models.DateField() # "2013-05-01",
    sol = models.IntegerField() #: 261,
    ls = models.FloatField() #: 310.5,
    min_temp = models.FloatField('low temp in Centigrade') #: -69.75,
    min_temp_fahrenheit = models.FloatField('low temp in Fahrenheit') #: -93.55,
    max_temp = models.FloatField('high temp in Centigrade') #": -4.48,
    max_temp_fahrenheit = models.FloatField('high temp in Fahrenheit') #": 23.94,
    pressure = models.FloatField() # : 868.05,
    pressure_string = models.CharField("pressure descriptor", max_length=100) # "Higher",
    abs_humidity = models.FloatField('absolute humidity') #: null,
    wind_speed = models.FloatField()  #: 2.0
    wind_direction = models.CharField # "--", this appears to almost always be null
    atmo_opacity = models.CharField('atmospheric conditions',max_length=100) #: "Sunny",
    season = models.CharField(max_length=10)#: "Month 11",
    sunrise = models.DateTimeField() #": "2013-05-01T11:00:00Z",
    sunset = models.DateTimeField() # "2013-05-01T22:00:00Z"
# end Weather model