from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Languages

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def languages_index(request):
    # languages = Languages.objects.all()
    languages = Languages.objects.filter(user=request.user)
    return render(request, 'languages/index.html', { 'languages': languages })


class LanguagesCreate(LoginRequiredMixin, CreateView):
    model = Languages
    fields = '__all__'
    success_url = '/languages'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LanguagesUpdate(LoginRequiredMixin, UpdateView):
    model = Languages
    success_url = '/languages'
    fields = '__all__'

class LanguagesDelete(LoginRequiredMixin, DeleteView):
    model = Languages
    success_url = '/languages'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
