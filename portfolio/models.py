from django.db import models
from PIL import Image


class Project(models.Model):
    project_title = models.CharField(max_length=50)
    description = models.TextField()
    imgproject = models.ImageField(upload_to = 'project_folder')
    img = models.ImageField(upload_to = 'project_folder')
    link = models.URLField( blank=True)

    def  __str__(self):
        return self.project_title

class Certificate(models.Model):
    certificate_title = models.CharField(max_length=50)
    certificate_description = models.TextField()
    imgcertificate = models.ImageField(upload_to = 'certificate_folder')
    imgc = models.ImageField(upload_to = 'certificate_folder')
    certificate_link = models.URLField( blank=True)

    def  __str__(self):
        return self.certificate_title


class Design(models.Model):
    design_title = models.CharField(max_length=50)
    design_description = models.TextField()
    imgdesign = models.ImageField(upload_to = 'design_folder')
    imgd = models.ImageField(upload_to = 'design_folder')

    def  __str__(self):
        return self.design_title
