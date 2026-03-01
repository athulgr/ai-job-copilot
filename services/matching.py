from django.db import connection
from resumes.models import Resume
from jobs.models import Job

def get_top_matching_jobs(resume_id, limit=5):
    resume = Resume.objects.get(id=resume_id)

    if resume.embedding is None:
        return []

    vector = [float(x) for x in resume.embedding]

    query = """
    SELECT id, title, company,
           embedding <-> %s::vector AS distance
    FROM jobs_job
    WHERE embedding IS NOT NULL
    ORDER BY embedding <-> %s::vector
    LIMIT %s;
"""

    with connection.cursor() as cursor:
        cursor.execute(query, [vector, vector, limit])
        rows = cursor.fetchall()

    return rows