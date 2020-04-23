from django.urls import path
from .views import LandingView, TeamView, TeamMemberView
from . import views

urlpatterns = [
    path('', LandingView.as_view(), name='home-landing'),
    path('team', TeamView.as_view(), name='home-team'),
    path('team/<str:username>', TeamMemberView.as_view(), name='home-team-member'),
]
