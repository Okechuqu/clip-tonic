from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
# Register your models here.


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteInfo.objects.exists():
            return False
        return True


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Social.objects.exists():
            return False
        return True


@admin.register(HowTo)
class HowToAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HowTo.objects.exists():
            return False
        return True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
