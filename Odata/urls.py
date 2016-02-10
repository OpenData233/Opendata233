from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Odata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^blog/', include('andablog.urls', namespace='andablog')),
    url(r'^feedreader/', include('feedreader.urls', namespace='feedreader')),
    url(r'^contact/', include('contact_form.urls', namespace='contact')),



]
