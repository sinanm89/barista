from django.conf.urls import patterns, url
from barista.restaurants.views import EligibleRestaurantsListView, ResultView

urlpatterns = patterns('',
                url(r'^$', EligibleRestaurantsListView.as_view(), name='daily_restaurants'),
                url(r'^results/$', ResultView.as_view(), name="results"),
                #
                # url(r'^search/$', StreamSearchPhotosListView.as_view(), name="stream_search_photos"),
                # url(r'^search/photos/(?P<pk>[-\d]+)/$', SearchPhotosDetailView.as_view(), name="stream_search_photo_detail"),
                # url(r'^search/photos/(?P<pk>[-\d]+)/adverts/$', StandaloneAdvertView.as_view(), name="search_photo_gallery_advert"),
                #
                # url(r'^(?P<slug>[-\w]+)/$', StreamDetailView.as_view(), name="stream_detail"),
                # url(r'^(?P<slug>[-\w]+)/upload/$', StreamPhotoUploadView.as_view(), name="stream_upload_photo"),
                # url(r'^(?P<slug>[-\w]+)/(?P<action>[-\w]+)/$', StreamDetailView.as_view(), name="stream_action"),
                # url(r'^(?P<slug>[-\w]+)/photos/(?P<pk>[-\d]+)/$', StreamPhotoDetailView.as_view(), name="photo_gallery"),
                # url(r'^(?P<slug>[-\w]+)/photos/(?P<pk>[-\d]+)/adverts/$', StandaloneAdvertView.as_view(), name="photo_gallery_advert"),
              )
