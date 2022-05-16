from rest_framework import serializers
from demo.models import PhotoFeedModel

class FindPhotoFeedSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(source='get_image_url')

    # def get_image_url(self, instance):
    #     return instance.image.url

    class Meta:
        model = PhotoFeedModel
        fields = [
            'id',
            'description',
            'image'
        ]