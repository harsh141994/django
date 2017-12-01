# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models import Q

from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.db import models
from .validators import validate_category
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL#to get the user model 
# Create your models here.

class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(location__iexact=query)|
                Q(category__icontains=query)|
                Q(category__iexact=query)|
                Q(item__name__icontains=query)|
                Q(item__contents__icontains=query)
                ).distinct()
        return self


class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)

    def search(self, query): #RestaurantLocation.objects.search()
        return self.get_queryset().search(query)

class RestaurantLocation(models.Model):#Model is the class it is inheriting from
	owner 			= models.ForeignKey(User) #one user has a lot of different locations
	name 			= models.CharField(max_length=150)
	location 		= models.CharField(max_length=150, null = True, blank = True)
	category 		= models.CharField(max_length=150, null = True, blank = True, validators=[validate_category])#since null=true so when we add a new field with this, we dont need to provide a value to the existing objects
	timestamp		= models.DateTimeField( auto_now_add = True) #automatically saved for us
	updated 		= models.DateTimeField(auto_now = True)
	slug			= models.SlugField(null = True, blank = True)

	objects = RestaurantLocationManager()


	def __str__(self): #if we want to print the restaurantlocation object
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'slug': self.slug}) #restaurants:detail, here restaurants is the namespace

	@property
	def title (self):
		return self.name	

#when you are saving the data to database -

def rl_pre_save_receiver(sender, instance, *args, **kwargs): #before saving to the database, this method is called
#instance is the object that we are going to store in the database
	instance.category = instance.category.capitalize()
	print "saving..."
	print instance.timestamp
	if not instance.slug: #if slug is not there then create a new instance
		instance.slug = unique_slug_generator(instance)



pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
