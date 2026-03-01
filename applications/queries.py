from django.db.models import Count
from .models import Application


def get_application_counts(user):
    """
    Returns application counts grouped by status
    """

    counts = (
        Application.objects
        .filter(user=user)
        .values("status")
        .annotate(total=Count("id"))
    )

    return {item["status"]: item["total"] for item in counts}


def get_pipeline_summary(user):
    """
    Returns full pipeline summary for dashboard
    """

    total = Application.objects.filter(user=user).count()

    interview = Application.objects.filter(
        user=user,
        status="interview"
    ).count()

    offer = Application.objects.filter(
        user=user,
        status="offer"
    ).count()

    rejected = Application.objects.filter(
        user=user,
        status="rejected"
    ).count()

    applied = Application.objects.filter(
        user=user,
        status="applied"
    ).count()

    pending = Application.objects.filter(
        user=user,
        status="pending"
    ).count()

    return {
        "total_applications": total,
        "pending": pending,
        "applied": applied,
        "interview": interview,
        "offer": offer,
        "rejected": rejected,
    }