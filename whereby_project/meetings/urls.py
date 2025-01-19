from django.urls import path
from .views import meeting

urlpatterns = [
    path('meeting/', meeting, name='meeting'),
    path('whereby-webhook/', whereby_webhook, name='whereby_webhook'),
]

