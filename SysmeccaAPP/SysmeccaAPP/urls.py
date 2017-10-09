"""
Definition of urls for SysmeccaAPP.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', SysmeccaAPP.views.home, name='home'),
    # url(r'^SysmeccaAPP/', include('SysmeccaAPP.SysmeccaAPP.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('HomeApp.urls')),
    url(r'^contacts/', include('ContactsApp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)