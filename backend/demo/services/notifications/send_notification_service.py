from demo.models import NotificationModel
from demo.dtos import SendNotificationDTO
from app.pusher import pusher_client

class SendNotificationService:
    @staticmethod
    def handler(dto: SendNotificationDTO):

        title = __class__.get_title(
            dto.title,
            dto.username,
            dto.type
        )

        notification = NotificationModel.objects.create(
            title = dto.title,
            type = dto.type,
            description = dto.description,
            url = dto.url,
            recipients = [],
            username = dto.username
        )

        notification.save()

        # Consider trigger a multiples canales -> canales por usuario?
        # user_notification_channel **
        pusher_client.trigger(
            u'notification_channel',
            u'new_notification',
            {
                u'title': dto.title,
                u'description': dto.description,
                u'url': dto.url,
                u'type': dto.type,
                u'username': dto.username,
                u'seen': dto.seen
            }
        )

    @staticmethod
    def get_title(title: str, username: str, type: str) -> str:
        result_type = ''
        if type == 'upload':
            result_type = 'ha subido'

        result = username + ' ' + \
                result_type + ' ' + \
                title

        return result