from django.contrib import admin

# Register your models here.
from .models import User, Plan  # Replace `MyModel` with the name of your model

admin.site.register(User)
admin.site.register(Plan)
