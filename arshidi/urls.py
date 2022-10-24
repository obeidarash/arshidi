from django.contrib import admin
from django.urls import path, include
from .view import home
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', home, name='home')
]

admin.site.site_header = "Admin Area"
admin.site.site_title = "Arshidi"
admin.site.index_title = "Welcome to Arshidi"
# handler404 = 'scam.views.error_404'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
