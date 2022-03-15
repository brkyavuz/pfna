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


def get_template_detail(request, template_name):
    template_path =  f"{BASEDIR}/config-templates/{template_name}"
    with open(template_path) as file:
        context = {"active_page":"config-management", "data":file.read()}
        return render(request, 'views/config-management/config-templates.html', context=context)

def templatesView(request):
    
    templates = Template.objects.all().values()
    
    context = {"active_page":"config-management", "data":templates}

    return render(request, 'views/config-management/config-templates.html', context=context)