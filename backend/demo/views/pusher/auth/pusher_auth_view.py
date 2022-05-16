import json
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from app.pusher import pusher_client
from django.http import JsonResponse
from rest_framework.views import APIView

class PusherAuthView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            channel = request.GET.get('channel_name', None)
            socket_id = request.GET.get('socket_id', None)

            auth = pusher_client.authenticate(
                channel = channel,
                socket_id = socket_id
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                data={'response': 'Error'},
                status=HTTP_400_BAD_REQUEST
            )

        return JsonResponse(
            data=json.dumps(auth),
            status=HTTP_200_OK,
            safe=False
        )
