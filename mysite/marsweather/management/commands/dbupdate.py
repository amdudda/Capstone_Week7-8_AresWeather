'''
This takes data I gleaned from the API and saves it to the database.
see https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
for how to set this up.  I left out _private.py since I don't seem to need it.
'''
from ...models import Weather
from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta
from .dbsetup import load_api_data

class Command(BaseCommand):
    help = 'Fetches new data from MAAS website by requesting data from after last available terrestrial date.'

    def handle(self, *args, **options):
        '''
        this handles the dbupdate command by looking up the last available terrestrial_date of data, then passing
        the next date to the url argument so it can request fresh data from the API.
        :param args:
        :param options:
        :return:
        '''

        # Make sure database is not empty before requesting & importing fresh data.
        if (len(Weather.objects.all()) == 0):
            print("Database has no records.  Please invoke 'python manage.py dbsetup' to import entire dataset.")
        else:
            # calculate the appropriate date and concatenate our target url
            update_url = 'http://marsweather.ingenology.com/v1/archive/?terrestrial_date_start='
            start_date = Weather.objects.order_by('-terrestrial_date')[:1][0].terrestrial_date
            start_date += timedelta(days=1)
            update_url += str(start_date)
            print("Requesting data using start date: %s." % str(start_date))

            # request and store updated data
            load_api_data(update_url)
        # end if-else
    # end Command handler
# end Command