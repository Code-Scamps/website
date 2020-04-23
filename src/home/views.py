from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from django.contrib.auth.models import User
from .models import Project


class LandingView():
    template_name = 'blog/landing.html'


class TeamView(ListView):
    model = User
    template_name = 'blog/team.html'
    context_object_name = 'members'
    ordering = ['date']


class TeamMemberView(ListView):
    model = Project
    template_name = 'blog/team-member.html'
    context_object_name = 'projects'
    ordering = ['-date']
    paginate_by = 10
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date')
