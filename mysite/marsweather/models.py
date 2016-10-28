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
    ls = models.FloatField(null=True) #: 310.5,
    min_temp = models.FloatField('low temp in Centigrade',null=True) #: -69.75,
    min_temp_fahrenheit = models.FloatField('low temp in Fahrenheit',null=True) #: -93.55,
    max_temp = models.FloatField('high temp in Centigrade',null=True) #": -4.48,
    max_temp_fahrenheit = models.FloatField('high temp in Fahrenheit',null=True) #": 23.94,
    pressure = models.FloatField(null=True) # : 868.05,
    pressure_string = models.CharField("pressure descriptor", max_length=100,null=True,blank=True) # "Higher",
    abs_humidity = models.FloatField('absolute humidity',null=True) #: null,
    wind_speed = models.FloatField(null=True)  #: 2.0
    wind_direction = models.CharField(max_length=100,null=True) # "--", this appears to almost always be null
    atmo_opacity = models.CharField('atmospheric conditions',max_length=100,null=True) #: "Sunny",
    season = models.CharField(max_length=10,null=True,blank=True)#: "Month 11",
    sunrise = models.DateTimeField(null=True) #": "2013-05-01T11:00:00Z",
    sunset = models.DateTimeField(null=True) # "2013-05-01T22:00:00Z"

    def __str__(self):
        # TODO clean this up so it returns prettier data, but it works for now
        data = {'terrestrial date':self.terrestrial_date,'sol':self.sol,'lowInC': self.min_temp,'hiInC':self.max_temp,'wind_speed':self.wind_speed,'atmospheric conditions': self.atmo_opacity}
        output = ''
        for key in data:
            output += str(key) + ": " + str(data[key]) + "\n"
        return str(output)

    def htmlify(self):
        output = "<h3>The weather for sol " + self.sol + " is:</h3>"
        output += "Low temp: " + self.min_temp + "C (" + self.min_temp_fahrenheit + "F)<br/>"
        output += "High temp: " + self.max_temp + "C (" + self.max_temp_fahrenheit + "F)<br/>"
        output += "Wind speed: " + self.wind_speed + "kph<br/>"
        atmocond = "n/a"
        if (self.atmo_opacity != 'None'): atmocond = self.atmo_opacity
        output += "Skies are: " + atmocond + "<br/>"
        output += "(date: " + self.terrestrial_date + ")<br/>"
        return output
# end Weather model

if (__name__ == "__main__"):
    print(Weather.objects.all())