from django.urls import path
import event.views

urlpatterns = [
    path('', event.views.event, name='event'),
]
