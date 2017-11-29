# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ItemForm #importing form from "forms"
from .models import Item


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)#filter by the user(given in the request)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):
    template_name = 'form.html'
    form_class = ItemForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Item'
        return context


class ItemUpdateView(UpdateView):
    template_name = 'form.html' #using from the outside form in templates
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context