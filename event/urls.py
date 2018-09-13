from django.urls import path
import event.views

urlpatterns = [
    path('', event.views.event_list, name='event_list'),
    path('<int:id>/', event.views.event_detail, name='event_detail'),
]
