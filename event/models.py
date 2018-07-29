from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True)
    address = models.TextField(blank=True)
    artist = models.TextField(blank=True)
    music = models.TextField(blank=True)
    price = models.TextField(blank=True)
    organizer = models.TextField(blank=True)
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name
