from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=256, name='event-name')
    time = models.DateTimeField(name='event-time')
    owner = models.ForeignKey(User, models.CASCADE, related_name='events')
