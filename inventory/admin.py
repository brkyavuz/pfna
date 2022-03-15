from django.contrib import admin
from inventory.models import Group, Host, Data

# Register your models here.
admin.site.register(Host)
admin.site.register(Group)
admin.site.register(Data)