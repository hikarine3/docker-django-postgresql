from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Country
from .models import Prefecture

admin.site.register(Country)
admin.site.register(Prefecture)
