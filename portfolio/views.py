from django.shortcuts import render
from django.views import View
from .models import *


def project (request, project_title):
    project = Project.objects.get(project_title=project_title)
    return render(request, 'portfolio/project.html', context={'project':project})


def certificate (request,certificate_title):
    certificate = Certificate.objects.get(certificate_title=certificate_title)
    return render(request, 'portfolio/certificate.html', context={'certificate':certificate})

def design (request,design_title):
    design = Design.objects.get(design_title=design_title)
    return render(request, 'portfolio/design.html', context={'design':design})


def portfolio (request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    designs = Design.objects.all()
    context = {
    'projects':projects,
    'certificates':certificates,
    'designs':designs,
    }
    return render(request, 'portfolio/index.html', context=context)
