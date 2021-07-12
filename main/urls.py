from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name = 'dashboard'),
	path('logout/', views.logout, name= 'logout'),
	path('members/', views.members, name = 'members'),
	path('loans/', views.loans, name = 'loans'),
	# path('savings/', views.savings, name = 'saving'),
	path('saved/', views.saved, name = 'saved'),
	# path('delete/<int:id>', views.delete),
	# path('edit/<int:id>', views.edit),
]






