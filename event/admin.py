from django.contrib import admin
from .models import Event, EventImage

# Register your models here.


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    inlines = [EventImageInline]
