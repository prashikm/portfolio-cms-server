from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# project link
# tags


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f'{self.title} - {self.user.username}'
