from django.contrib import admin

from apps.story.models import Story, Event

admin.site.register(Story)
admin.site.register(Event)
