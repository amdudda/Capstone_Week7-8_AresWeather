from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
]

# regex101.com might help with future development.