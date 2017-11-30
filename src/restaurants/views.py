# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #mixins are for class based views
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):
	
	def get_queryset(self): 
		queryset = RestaurantLocation.objects.filter(owner=self.request.user) #owner being the logged in user
		#that is get this for the current logged in user
		return queryset #collection of RestaurantLocation database objects


class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self): 
		queryset = RestaurantLocation.objects.filter(owner=self.request.user) #owner being the logged in user
		#that is get this for the current logged in user
		return queryset 
	
		

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'form.html'
	#success_url = "/restaurants/"

	#createview runs form_valid method
	def form_valid(self, form):
		instance = form.save(commit=False) #saving the form and getting the object
		instance.owner = self.request.user #setting the owner for that RestaurantLocation object to the user from the request
		return super(RestaurantCreateView, self).form_valid(form)#validating the form 

	#using this function so that we have the context and that we can use to put the title in the 
	#forms.html (instead of hardcoding the name there)	
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'restaurants/detail-update.html'
	#success_url = "/restaurants/"

	#using this function so that we have the context and that we can use to put the title in the 
	#forms.html (instead of hardcoding the name there)	
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Restaurant'
		return context

	def get_queryset(self): 
		queryset = RestaurantLocation.objects.filter(owner=self.request.user) #owner being the logged in user
		#that is get this for the current logged in user
		return queryset 	
