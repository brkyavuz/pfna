from django.urls import path
from .views import inventoryView

app_name = 'inventory'

urlpatterns =[
    path('', inventoryView, name='inventory')
]