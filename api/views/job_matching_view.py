from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from resumes.models import Resume
from jobs.models import Job
from api.serializers.job_serializer import JobSerializer


class JobMatchingAPI(ListAPIView):

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        resume = Resume.objects.filter(user=self.request.user).order_by("-created_at").first()

        if not resume:
            return Job.objects.none()

        return Job.objects.raw(
            """
            SELECT *
            FROM jobs_job
            ORDER BY embedding <-> %s::vector
            LIMIT 100
            """,
            [resume.embedding.tolist()],
        )