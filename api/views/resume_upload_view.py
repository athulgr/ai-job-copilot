from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from resumes.models import Resume
from api.serializers.resume_serializer import ResumeUploadSerializer

from sentence_transformers import SentenceTransformer


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


class ResumeUploadAPI(CreateAPIView):

    queryset = Resume.objects.all()

    serializer_class = ResumeUploadSerializer

    permission_classes = [IsAuthenticated]

    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):

        resume = serializer.save(user=self.request.user)

        # Read file safely
        file = resume.file.read()

        try:
            text = file.decode("utf-8", errors="ignore")
        except:
            text = ""

        embedding = model.encode(text)

        resume.embedding = embedding.tolist()

        resume.save()