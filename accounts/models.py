from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from pgvector.django import VectorField


class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Future-ready fields for our platform
    linkedin_url = models.URLField(blank=True, null=True)
    naukri_url = models.URLField(blank=True, null=True)
    auto_apply_enabled = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
