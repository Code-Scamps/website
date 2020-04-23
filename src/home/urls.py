from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LandingView, TeamView, TeamMemberView
from . import views
from users import views as user_views

urlpatterns = [
    path('', LandingView.as_view(), name='home-landing'),
    path('team', TeamView.as_view(), name='home-team'),
    path('team/<str:username>', TeamMemberView.as_view(), name='home-team-member'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
