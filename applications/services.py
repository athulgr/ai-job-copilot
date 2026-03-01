from django.utils import timezone
from .models import Application


VALID_TRANSITIONS = {
    "pending": ["applied"],
    "applied": ["interview", "rejected"],
    "interview": ["offer", "rejected"],
    "offer": [],
    "rejected": [],
}


def update_application_status(application: Application, new_status: str):
    current_status = application.status

    if new_status not in VALID_TRANSITIONS[current_status]:
        raise ValueError(
            f"Invalid transition from {current_status} to {new_status}"
        )

    application.status = new_status

    if new_status == "applied":
        application.applied_at = timezone.now()

    application.save()
    return application