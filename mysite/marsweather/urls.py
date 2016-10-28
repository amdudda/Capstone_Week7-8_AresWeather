from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sol_id>[0-9]+)/$', views.sol , name='sol'),
    url(r'^about', views.about, name='about')
]

# regex101.com might help with future development.