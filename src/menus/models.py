# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from restaurants.models import RestaurantLocation

class Item(models.Model):
    # associations
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)#every item has an user
    restaurant      = models.ForeignKey(RestaurantLocation)    #every item has a restaurant
    # item stuff
    name            = models.CharField(max_length=120)
    contents        = models.TextField(help_text='Separate each item by comma')
    excludes        = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
		return reverse('menus:detail', kwargs={'pk': self.pk}) #restaurants:detail, here restaurants is the namespace
    
    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")#returning the list of contents of the current(self) object(item)

    def get_excludes(self):
        return self.excludes.split(",")