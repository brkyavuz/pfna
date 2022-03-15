from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=64,null=False, primary_key=True, unique=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(max_length=16, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)
    country = models.CharField(max_length=16, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.group_name
    
class Data(models.Model):
    name = models.CharField(max_length=64, null=False, primary_key=True)
    device_type = models.CharField(max_length=16)
    country = models.CharField(max_length=16, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)
    
    def __str__(self):
        return self.group_name

class Host(models.Model):
    name = models.CharField(max_length=64, null=False, primary_key=True)
    hostname = models.GenericIPAddressField(unique=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(max_length=16, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)
    port = models.PositiveBigIntegerField()
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name