from django.urls import path

from api.views.dashboard_view import DashboardSummaryAPI
from api.views.resume_upload_view import ResumeUploadAPI
from api.views.job_matching_view import JobMatchingAPI
from api.views.application_view import (
    ApplicationListCreateAPI,
    ApplicationUpdateAPI
)

urlpatterns = [
    path("dashboard/", DashboardSummaryAPI.as_view()),

    path("jobs/match/", JobMatchingAPI.as_view()),

    path("applications/", ApplicationListCreateAPI.as_view()),
    path("applications/<int:pk>/", ApplicationUpdateAPI.as_view()),
    path("resumes/upload/", ResumeUploadAPI.as_view()),
]