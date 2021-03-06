from django.urls import path
from django.contrib.auth import views as auth_views #installing preMade views form django
from . import views

urlpatterns = [
    #post views
    #previous login view
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

]