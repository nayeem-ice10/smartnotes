from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('authorized/', views.AuthorizeView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogOutInterfaceView.as_view(),name='logout'),
    path('register', views.SignupView.as_view(),name='register'),
]
