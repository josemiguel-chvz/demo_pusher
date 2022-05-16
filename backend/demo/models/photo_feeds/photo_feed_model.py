from django.db import models

class PhotoFeedModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='static/documents/')