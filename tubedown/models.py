from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class HowTo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)
    
    def __str__(self):
        return self.title

 
class Project(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    project = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Social(models.Model):
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    tiktok = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"Social Account"


class SiteInfo(models.Model):
    page_title = models.CharField(max_length=200, blank=True, null=True)
    favicon = models.ImageField(upload_to='image', blank=True , null=True)
    page_name = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return f"Site Information"
