from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('lifecodemohit.views',
    # Examples:
    # url(r'^$', 'lcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home'),
    url(r'^index$', 'index'),
)