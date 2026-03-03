from rest_framework import serializers
from applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
            "id",
            "user",
            "job",
            "resume",
            "status",
            "cover_letter",
            "notes",
            "applied_at",
            "created_at",
        ]
        read_only_fields = ["user", "created_at"]