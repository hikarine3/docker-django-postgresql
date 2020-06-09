from django.shortcuts import render
from .models import Country
from .models import Prefecture
from pprint import pprint
from django.core.paginator import Paginator

# Create your views here.
def index(request):
  pgsz = 3
  country_list = Country.objects.order_by('name')
  paginator = Paginator(country_list, pgsz)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'geo/index.html', { 'page_obj': page_obj })

def country_detail(request, countryKey):
  pgsz = 3
  countrySingleRecord = Country.objects.get(key=countryKey)
  prefecture_list = Prefecture.objects.filter(country=countrySingleRecord.id).order_by('name')
  paginator = Paginator(prefecture_list, pgsz)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'geo/countries/detail.html', { 'page_obj': page_obj })
