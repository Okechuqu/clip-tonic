from .models import *


def frontendContextProcessor(request):
    return {
        'howtos': HowTo.objects.all(),
        'projects': Project.objects.all(),
        'socials': Social.objects.all().first(),
        'siteinfos': SiteInfo.objects.all().first(),
    }
