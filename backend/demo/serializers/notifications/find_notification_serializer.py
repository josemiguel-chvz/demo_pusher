from rest_framework import serializers
from demo.models import NotificationModel

class FindNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = [
            'id',
            'title',
            'description',
            'type',
            'seen',
            'url',
            'username'
        ]