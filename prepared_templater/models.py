import hashlib
import re

from django.db import models

class EventTemplate(models.Model):
    event_template = models.ForeignKey('pretixbase.Event', on_delete=models.CASCADE)
    organizer = models.ForeignKey('pretixbase.Organizer', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

class SyncedEvent(models.Model):
    event = models.ForeignKey('pretixbase.Event', on_delete=models.CASCADE)
    event_template = models.ForeignKey('prepared_templater.EventTemplate', null=True, on_delete=models.CASCADE)
    name = models.TextField()
    comment = models.TextField(blank=True)
