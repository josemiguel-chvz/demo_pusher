from demo.dtos import SendNotificationDTO
from demo.services import SendNotificationService
from demo.forms.photo_feeds.create_photo_feed_form import CreatePhotoFeedForm
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from app.pusher import pusher_client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class CreatePhotoFeedView(APIView):

    @csrf_exempt
    def post(self,request,*args,**kwargs):
        try:
            form = CreatePhotoFeedForm(
                data=request.POST,
                files=request.FILES
            )

            if not form.is_valid():
                return JsonResponse(
                    data={k: v.get_json_data() for k, v in form.errors.items()},
                    status=HTTP_400_BAD_REQUEST
                )

            # Servicio
            f = form.save()
            pusher_client.trigger(
                u'photo_feed_channel',
                u'new_image',
                {
                    u'description': f.description,
                    u'image': f.image.url
                }
            )

            dto = SendNotificationDTO(
                type="upload",
                title="nueva imagen",
                description= f.image.url,
                url="https://google.cl",
                recipients=[],
                username='usuario prueba',
                seen=False
            )

            SendNotificationService.handler(dto)

        except Exception as e:
            print(str(e))
            return JsonResponse(
                data={'response': 'Error'},
                status=HTTP_400_BAD_REQUEST
            )
        return JsonResponse(
            data={'response': True},
            status=HTTP_200_OK
        )