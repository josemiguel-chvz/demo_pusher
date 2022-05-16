from django.db import models
from django.contrib.auth.models import User

class MessageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # username = models.CharField(blank=True, null=True, max_length=)
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)
    created_at = models.DateTimeField(auto_now=True)