from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from pgvector.django import VectorField

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes"
    )

    version = models.IntegerField(default=1)

    file = models.FileField(upload_to="resumes/")

    parsed_data = models.JSONField(blank=True, null=True)

    embedding = VectorField(dimensions=384, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - v{self.version}"