from django.urls import path
from .views import *

urlpatterns = [


path('', portfolio, name='portfolio'),
path('certificate/<str:certificate_title>', certificate, name='certificate'),
path('design/<str:design_title>', design, name='design'),
path('portfolio/project/<str:project_title>', project, name='project'),


]
