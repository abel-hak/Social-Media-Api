from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    bio = models.TextField(blank=True)

    # Override the `groups` and `user_permissions` fields to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
