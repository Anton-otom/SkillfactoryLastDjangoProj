from django.shortcuts import render
from .models import Advertisement
from django.views.generic import ListView


class AdvertisementList(ListView):
    model = Advertisement
    ordering = '-created_at'
    template_name = 'advertisements/advertisements.html'
    context_object_name = 'advertisements'
    paginate_by = 10
