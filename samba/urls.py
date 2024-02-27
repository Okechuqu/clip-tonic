from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from tubedown.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('youtube/', youtube, name="youtube"),
    path('twitter/', twitter, name="twitter"),
    path('tiktok/', tiktok, name="tiktok"),
    path('instagram/', instagram, name="instagram"),
    path('facebook/', facebook, name="facebook"),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    