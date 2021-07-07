from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name = 'dashboard'),
	path('logout/', views.logout, name= 'logout'),
	path('members/', views.members, name = 'members'),
	path('delete/<int:id>', views.delete),
	path('edit/<int:id>', views.edit),
]






