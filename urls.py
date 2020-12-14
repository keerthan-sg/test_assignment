from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.login,name='login'),
    path('ticket',views.ticket,name='ticket'),
    path('submit_ticket',views.submit_ticket,name='submit_ticket')
]
