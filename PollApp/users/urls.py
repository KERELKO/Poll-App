from django.urls import path  
from . import views


app_name = 'users'

urlpatterns = [
	path('login/', views.UserLoginView.as_view(),
		 name='login'),
	path('logout/', views.UserLogout.as_view(),
      	 name='logout'),
	path('registration/', views.UserRegistrationView.as_view(),
		 name='registration'),
]
