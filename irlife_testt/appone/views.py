from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)



class index(ListView):

    model=models.IrList

class detaillist(DetailView):

    context_object_name = 'ir_details'
    model=models.IrList
    template_name='appone/irlist_detail.html'
# Create your views here.
class createir(CreateView):
    fields= ("irno","rfc")
    model=models.IrList

class irUpdateView(UpdateView):
    fields = ("rfc",)
    model = models.IrList

class irDeleteView(DeleteView):
    model = models.IrList
    success_url = reverse_lazy("appone:index")
