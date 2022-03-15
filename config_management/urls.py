from django.urls import path
from .views import getconfigView
from .views import sendconfigView

app_name = 'config_management'

urlpatterns =[
    path('get-config', getconfigView, name='get_config'),
    path('send-config', sendconfigView, name='send_config')
]