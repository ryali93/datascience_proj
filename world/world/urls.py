from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('', include('cities.urls')),
    url(r'^cities/', include('cities.urls')),
    url('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()