from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from barista.views import BaristaHomeView

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', BaristaHomeView.as_view()),
    # url(r'^barista/', include('barista.foo.urls')),

    url(r'^food/', include('barista.restaurants.urls', namespace="lunchtime")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
