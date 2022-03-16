from django.urls import path
from .views import getconfigView,sendconfigView,templatesView,template_get

app_name = 'config_management'

urlpatterns =[
    path('config-get', getconfigView, name='config-get'),
    path('config-send', sendconfigView, name='config-send'),
    path('config-templates', templatesView, name='config-templates'),
    path('config-templates/<str:template_name>', template_get, name='template-get'),
]