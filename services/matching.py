from django.db import connection
from resumes.models import Resume
from jobs.models import Job


def get_top_matching_jobs(resume_id, limit=5):
    resume = Resume.objects.get(id=resume_id)

    if not resume.embedding:
        return []

    query = """
        SELECT id, title, company,
               embedding <-> %s AS distance
        FROM jobs_job
        WHERE embedding IS NOT NULL
        ORDER BY embedding <-> %s
        LIMIT %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [resume.embedding, resume.embedding, limit])
        rows = cursor.fetchall()

    return rows