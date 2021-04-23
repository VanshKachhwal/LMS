from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "LMS Admin"
admin.site.site_title = "LMS Admin Panel"
admin.site.index_title = "Welcome to LMS Admin Panel"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^library/', include('library.urls')),
    url(r'^lms/', include('library.urls')), 
    url(r'^', include('library.urls')),
    
    ##Social-auth
    path('social-auth/', include('social_django.urls', namespace='social'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
