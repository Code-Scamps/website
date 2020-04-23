from django.urls import path
from .views import LandingView
from . import views

urlpatterns = [
    path('', LandingView.as_view(), name='home-landing'),
]
