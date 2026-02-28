from django.db import models
from pgvector.django import VectorField


class Job(models.Model):
    SOURCE_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("naukri", "Naukri"),
        ("indeed", "Indeed"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField()

    source_platform = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES,
        default="other"
    )

    external_job_id = models.CharField(max_length=255, blank=True, null=True)
    job_url = models.URLField(blank=True, null=True)

    embedding = VectorField(dimensions=384, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"