from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company",
            "location",
            "source_platform",
            "job_url",
            "created_at",
        ]