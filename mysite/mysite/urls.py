from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^tsukkomi/submit/', 'tsukkomi.views.tsukkomi_submit'),
    url(r'^tsukkomi/', 'tsukkomi.views.tsukkomi_index'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += staticfiles_urlpatterns()
