from django.db import models
from django.conf import settings
from jobs.models import Job
from resumes.models import Resume


class Application(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("applied", "Applied"),
        ("rejected", "Rejected"),
        ("interview", "Interview"),
        ("offer", "Offer"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.ForeignKey(
        Resume,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="pending"
    )

    applied_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "job")

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"