from django.conf.urls import url

from . import views

urlpatterns =[
    # url(r'^savearray$', views.MWsavearray, name='MWsavearray'),
    url(r'^$', views.MWindex, name='MWindex'),
]

# regex101.com might help with future development.