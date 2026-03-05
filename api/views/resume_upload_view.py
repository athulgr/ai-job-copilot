from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


from resumes.models import Resume
from api.serializers.resume_serializer import ResumeUploadSerializer
from resumes.parser import extract_text
from sentence_transformers import SentenceTransformer


from services.parser import extract_text
from services.embedding import generate_embedding


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


class ResumeUploadAPI(CreateAPIView):

    queryset = Resume.objects.all()

    serializer_class = ResumeUploadSerializer

    permission_classes = [IsAuthenticated]

    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        
        resume = serializer.save(user=self.request.user)

        text = extract_text(resume.file)

        embedding = generate_embedding(text)

        resume.embedding = embedding

        resume.save()

   
   
    



        

    