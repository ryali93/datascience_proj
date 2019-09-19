from django.conf.urls import url
from . views import CitiesDetailView, index


app_name = 'cities'

urlpatterns = [
    url('^$', index, name='index'),
    # city detail view
    url(r'^city/(?P<pk>[0-9]+)$',
        CitiesDetailView.as_view(), name='city-detail'),
]