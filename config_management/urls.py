from django.urls import path
from .views import getconfigView,sendconfigView,templatesView,get_template_detail

app_name = 'config_management'

urlpatterns =[
    path('config-get', getconfigView, name='config-get'),
    path('config-send', sendconfigView, name='config-send'),
    path('config-templates', templatesView, name='config-templates'),
    path('config-templates/<str:template_name>', get_template_detail, name='template-detail'),
]