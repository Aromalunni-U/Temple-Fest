from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name = "index"),
    path('about',about,name = "about"),
    path('request',request,name = "request"),
    path('services',services,name = "services"),
    path('servicedetail',servicedetail,name = "servicedetail"),
    path('providerpnl',providerpnl,name = "providerpnl"),
    path('profile',profile,name = "profile"),
    path('profile_edit/<int:id>/',profile_edit,name = "profile_edit"),

    path('service/<int:pk>/', view_service, name='view_service'),
    path('messages',message,name = "messages"),
    path('book/', book, name='booking-form'), 
    path('view_request/<int:id>/', view_request, name='view_request'),
    path('booking/<int:id>/accept/', accept_booking, name='accept_booking'),
    path('booking/<int:id>/reject/', reject_booking, name='reject_booking'),
    path('bookings', bookings, name='bookings'), 

    path('message/<int:message_id>/',message_detail, name='message_detail'),
    path('compose/', compose_message, name='compose_message'),




]
