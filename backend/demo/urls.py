from django.urls import path

from demo.views.pusher import PusherAuthView
from demo.views import CreatePhotoFeedView, FindPhotoFeedView, FindNotificationsView

urlpatterns = [
    path('photo-feed', CreatePhotoFeedView.as_view()),
    path('photo-feed/all', FindPhotoFeedView.as_view()),
    path('notification/all', FindNotificationsView.as_view()),
    path('pusher/auth', PusherAuthView.as_view())
]