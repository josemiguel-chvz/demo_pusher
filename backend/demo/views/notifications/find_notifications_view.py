from demo.serializers import FindNotificationSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import JsonResponse
from demo.models import NotificationModel
from django.views.decorators.csrf import csrf_exempt

class FindNotificationsView(APIView):

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        all_notifications = []
        try:
            all_notifications = NotificationModel.objects.all().order_by('-id')
            serializer = FindNotificationSerializer(all_notifications, many=True)
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