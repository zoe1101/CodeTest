from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usagedemo/', include('usagedemo.urls')),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('bookmanagement/', include('bookmanagement.urls')),
    path('', include('bookmanagement.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
