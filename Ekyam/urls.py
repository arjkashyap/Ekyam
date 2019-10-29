from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('visit.urls')),
    url(r'^', include('main.urls')),
    url(r'^mentors/', include('mentors.urls')),
    url(r'^startup/', include('startup.urls')),
    url(r'^enetwork/', include('enetwork.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

