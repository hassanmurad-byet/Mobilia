
from django.contrib import admin
from django.urls import path, include

from django.conf import  settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)