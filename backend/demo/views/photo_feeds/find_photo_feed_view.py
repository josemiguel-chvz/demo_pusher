from demo.serializers.photo_feeds.find_photo_feed_serializer import FindPhotoFeedSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import JsonResponse
from demo.models import PhotoFeedModel
from django.views.decorators.csrf import csrf_exempt

class FindPhotoFeedView(APIView):

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        all_images = []
        try:
            all_images = PhotoFeedModel.objects.all().order_by('-id')
            serializer = FindPhotoFeedSerializer(all_images, many=True)

        except Exception as e:
            print(str(e))
            return JsonResponse(
                data={'response': 'Error'},
                status=HTTP_400_BAD_REQUEST
            )
        return JsonResponse(
            data=serializer.data,
            status=HTTP_200_OK,
            safe=False
        )