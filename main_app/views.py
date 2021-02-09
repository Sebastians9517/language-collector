from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Languages

# Create your views here.
class LanguagesList(ListView):
    model = Languages

class LanguagesCreate(CreateView):
    model = Languages
    fields = '__all__'
    success_url = '/'

class LanguagesUpdate(UpdateView):
    model = Languages
    success_url = '/'
    fields = '__all__'

class LanguagesDelete(DeleteView):
    model = Languages
    success_url = '/'
