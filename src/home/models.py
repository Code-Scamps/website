from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
