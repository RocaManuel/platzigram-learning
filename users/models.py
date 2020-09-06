"""Users models"""

#Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model:

    proxy model that extends the base date with other User information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(
        max_length=200,
        blank=True
    )
    biography = models.TextField(
        blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Override string return"""
        return self.user.username

