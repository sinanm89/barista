from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
import django_kibrit
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from barista.views import BaristaHomeView

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="aerial/index.html")),

    url(r'^barista/', BaristaHomeView.as_view()),
    url(r'^amazonChallenge/', TemplateView.as_view(template_name="amazon.html")),
    # url(r'^barista/', include('barista.foo.urls')),

    url(r'^food/', include('barista.restaurants.urls', namespace="lunchtime")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
