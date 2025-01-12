from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register the User model to make it available in the admin interface
admin.site.register(User)
admin.site.register(Profile)