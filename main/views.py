from django.shortcuts import render, redirect 
from django.contrib.auth import logout as logouts, authenticate, login
from main.forms import LoaningForm, ListForm, SavingForm
from main.models import List, Loaning, Saving


def dashboard(request):
	return render (request, 'registration/dashboard.html')

# def loans(request):
# 	return render (request, 'registration/loans.html')

# def savings(request):
# 	return render (request, 'registration/savings.html')

# def save(request):
# 	return render (request, 'registration/save.html')

def logout(request):
	if request.method == 'POST':
		logouts(request)
		return redirect('/login')

def members (request):
	members = List.objects.all()
	return render (request, 'registration/members.html', {'members':members})

def loans (request):
	loans = Loaning.objects.all()
	return render (request, 'registration/loans.html', {'loans':loans})

def saved (request):
	saved = Saving.objects.all()
	return render (request, 'registration/save.html', {'saved':saved})

# def members (request):
# 	members = Members.objects.all()
# 	return render (request,'registration/members.html', {'members': members})

# def delete (request, id):
# 	members = Members.objects.get(id = id)
# 	members.delete()
# 	return redirect ('/members')

# def edit(request, id):
# 	members = Members.objects.get(id=id)
# 	return render(request, 'registration/edit.html', {'members':members})
