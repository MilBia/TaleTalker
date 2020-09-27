from django.contrib import admin

from apps.location.models import LocationType, Location

admin.site.register(LocationType)
admin.site.register(Location)
