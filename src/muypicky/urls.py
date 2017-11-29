"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


#need to import the views so as to connect to the url
from restaurants.views import  (restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    restaurant_createview,
    RestaurantCreateView
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'), #name is used in navigation html, so that whenever the url is changed here, we dont have to change that in the navigation also
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name = 'contact'),
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name = "home"), #import the TemplateView and 
    #add the template name as the argument (this works if we dont need to manipulate the view in the views)
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name = 'about'),
    url(r'^restaurants/', include('restaurants.urls', namespace = 'restaurants')),
    url(r'^items/', include('menus.urls', namespace = 'menus')),

 ]   