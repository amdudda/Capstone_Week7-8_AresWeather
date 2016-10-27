from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.MWindex, name='MWindex'),
]

# regex101.com might help with future development.