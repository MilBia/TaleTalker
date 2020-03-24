from django.contrib import admin
from .models import Character, Attribute, AttributeType

admin.site.register(Character)
admin.site.register(Attribute)
admin.site.register(AttributeType)
