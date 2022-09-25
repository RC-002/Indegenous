from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from .models import *

class home(ListView):
  template_name = "index.html"
  model = Info
  ordering = ["id"]
  context_object_name = "Info"

  def get_context_data(self,**kwargs):
    context = super(home,self).get_context_data(**kwargs)
    context['info'] = " "
    context['infoDetails'] = " "
    return context