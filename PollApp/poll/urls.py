from django.urls import path
from . import views


app_name = 'poll'

urlpatterns = [
	path('all/', views.PollListView.as_view(), 
		 name='all'),
	path('create/', views.PollCreateView.as_view(), 
		 name='create'),
	path('edit/<pk>/', views.PollEditView.as_view(), 
		 name='edit'),
	path('detail/<pk>/', views.PollDetailView.as_view(), 
		 name='detail'),
	path('delete/<pk>/', views.PollDeleteView.as_view(),
		 name='delete'),
	# auth
	path('login/', views.UserLoginView.as_view(),
		 name='login'),
	path('logout/', views.UserLogout.as_view(),
      	 name='logout'),
	path('registration/', views.UserRegistrationView.as_view(),
		 name='registration'),
]