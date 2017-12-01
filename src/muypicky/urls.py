from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'), #name is used in navigation html, so that whenever the url is changed here, we dont have to change that in the navigation also
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name = 'contact'),
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name = "home"), #import the TemplateView and 
    #add the template name as the argument (this works if we dont need to manipulate the view in the views)
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name = 'about'),
    url(r'^restaurants/', include('restaurants.urls', namespace = 'restaurants')),
    url(r'^items/', include('menus.urls', namespace = 'menus')),
    url(r'^u/', include('profiles.urls', namespace = 'profiles')),

 ]   