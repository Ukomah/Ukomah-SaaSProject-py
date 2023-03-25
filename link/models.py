from django.db import models

# Create your models here.
from accounts.models import User


class Category(models.models):
    name=models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    

class Link(models.model):
    category = models.ForeignKey(Category, related_name='links', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)