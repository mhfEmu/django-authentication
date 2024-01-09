from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
class RegisterView(CreateView):
	form_class = CustomUserCreationForm
	success_url = '/accounts/login'
	template_name = 'registration/signup.html'
	
