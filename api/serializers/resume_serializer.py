from rest_framework import serializers
from resumes.models import Resume


class ResumeUploadSerializer(serializers.ModelSerializer):

    file = serializers.FileField()

    class Meta:
        model = Resume
        fields = [
            "id",
            "file",
            "version",
            "parsed_data",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "parsed_data",
            "created_at",
        ]