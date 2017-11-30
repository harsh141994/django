from django.conf.urls import url


#need to import the views so as to connect to the url
from .views import  (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
    )

urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name = 'detail'),
  #  url(r'^(?P<slug>[\w-]+)/edit$', RestaurantUpdateView.as_view(), name = 'edit'),
    url(r'^$', RestaurantListView.as_view(), name = 'list'),


]
