from django.db import models
from django.contrib.postgres.fields import ArrayField


class NotificationModel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=20, blank=True)
    url = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=20, blank=True)
    recipients = ArrayField(
        models.UUIDField(),
        null=True
    )
    seen = models.BooleanField(null=True, default=False)
