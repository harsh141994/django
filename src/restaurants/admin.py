# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import RestaurantLocation #need to register modals in the admin so under the app name you can see your model name in the django app

admin.site.register(RestaurantLocation)
