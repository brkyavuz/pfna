from django.shortcuts import render
from nornir import InitNornir

# Create your views here.

def getconfigView(request):

    context = {"active_page":"config-management",}

    return render(request, 'views/config-management/get-config.html', context=context)

def sendconfigView(request):

    context = {"active_page":"config-management",}

    return render(request, 'views/config-management/send-config.html', context=context)
