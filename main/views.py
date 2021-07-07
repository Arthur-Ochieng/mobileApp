from django.shortcuts import render, redirect 
from django.contrib.auth import logout as logouts, authenticate, login
from main.forms import MembersForm
from main.models import Members


def dashboard(request):
	return render (request, 'registration/dashboard.html')

def logout(request):
	if request.method == 'POST':
		logouts(request)
		return redirect('/login')

def members (request):
	members = Members.objects.all()
	return render (request,'registration/view.html', {'members': members})

def delete (request, id):
	members = Members.objects.get(id = id)
	members.delete()
	return redirect ('/members')

def edit(request, id):
	members = Members.objects.get(id=id)
	return render(request, 'registration/edit.html', {'members':members})

	# if request.method == "POST":
	# 	form = MembersForm(request.POST)
	# 	if form.is_valid():
	# 		try:
	# 			form.save()
	# 			return redirect ('registration/dashboard.html')
	# 		except:
	# 			pass
	# else:
	# 	form = MembersForm()
	# return render (request, 'registration/members.html', {'form':form})
