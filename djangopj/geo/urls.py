from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='geo_index'),
    path('countries/<slug:countryKey>/', views.country_detail, name='country_detail')
]