from django.contrib import admin
from .models import providers,cities,hotels,amenities
# Register your models here.

admin.site.register(providers)
admin.site.register(cities)
admin.site.register(hotels)
admin.site.register(amenities)
