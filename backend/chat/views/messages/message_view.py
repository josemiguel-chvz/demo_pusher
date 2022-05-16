import json
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from app.pusher import pusher_client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat.models.messages import MessageModel

class MessageView(APIView):
    def post(self, request, *args, **kwargs):
        pass
    # @csrf_exempt
    # def post(self, request, *args, **kwargs):
    #     body = json.loads(request.body)
    #     # Service Logic
    #     message = MessageModel(
    #         message=body.get('message', ''),
    #         status='',
    #         username=body.get('username','')
    #     )
    #     message.save()
    #     pusher_message = {
    #         'id': message.id,
    #         'name': message.username,
    #         'status': message.status,
    #         'message': message.message
    #     }

    #     pusher_client.trigger(
    #         u'chat_channel',
    #         u'chat_message',
    #         pusher_message
    #     )

    #     return JsonResponse(
    #         data={'response': True},
    #         status=HTTP_200_OK