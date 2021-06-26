from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# # Create your views here.
# from .models import *
# from .forms import OrderForm, CreateUserForm



def dashboard(request):
    return render (request, 'main/dashboard.html')

def register(request):
    return render (request, 'main/register.html')

def login(request):
    return render (request, 'main/login.html')















# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'accounts/register.html', context)

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'accounts/login.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')











# from django.shortcuts import render, redirect
# from django.contrib.auth import login,authenticate
# from django.http import HttpResponse
# from .models import tb1_Authentication
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm

# from .forms import CreateUserForm

# def login(request):
#     context =  {}
#     return render (request, 'main/login.html', context)

# def register(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context =  {'form':form}
#     return render (request, 'main/register.html', context)

# def dashboard(request):
#     return render (request, 'main/dashboard.html')

