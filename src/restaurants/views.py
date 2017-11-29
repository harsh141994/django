# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm



def restaurant_createview(request):
	
	form = RestaurantLocationCreateForm(request.POST or None)
	errors=None
	
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurants")

	if form.errors:
		print form.errors	
		errors = form.errors
	template_name='restaurants/form.html'
	context={"form":form, "errors":errors} #can pass in the form itself so that we dont have to write the fields again in the html
	return render(request, template_name, context)



def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()#getting all the items in the restaurantlocation database
	context={
		"object_list":queryset #context is mostly like this
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	#template_name='restaurants/restaurants_list.html' #this template name we were overriding
	#currently no slug is being passed
	#therefore the call is just
	#queryset = RestaurantLocation.objects.all()

	def get_queryset(self): #getting the queryset(overriding the method from the superclass)
		slug = self.kwargs.get("slug") #slug is the dictionary object in the self.kwargs
		if slug:	
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact = slug)|
				Q(category__icontains = slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset #collection of RestaurantLocation database objects


class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	
		

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = "/restaurants/"

	#createview runs form_valid method
	def form_valid(self, form):
		instance = form.save(commit=False) #saving the form and getting the object
		instance.owner = self.request.user #setting the owner for that RestaurantLocation object to the user from the request
		return super(RestaurantCreateView, self).form_valid(form)#validating the form 

	