from django.http import JsonResponse
from django.shortcuts import render
from nornir import InitNornir
from pathlib import Path
from .models import Template

BASEDIR = Path(__file__).resolve().parent

def getconfigView(request):

    context = {"active_page":"config-management",}

    return render(request, 'views/config-management/config-get.html', context=context)

def sendconfigView(request):

    context = {"active_page":"config-management",}

    return render(request, 'views/config-management/config-send.html', context=context)


def template_get(request, template_name):
    qs = Template.objects.filter(template_name=template_name).values('template_name', 'template_content')
    
    return JsonResponse(qs[0])

def templatesView(request):
    
    qs = Template.objects.values('template_name', 'description', 'created', 'updated')
    
    context = {"active_page":"config-management", "data":qs}

    return render(request, 'views/config-management/config-templates.html', context=context)