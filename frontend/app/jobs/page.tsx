"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/lib/api";

interface Job {
  id: number;
  title: string;
  company: string;
  location: string;
  source_platform: string;
  job_url: string;
  created_at: string;
}

export default function JobsPage() {
  const router = useRouter();
  const [jobs, setJobs] = useState<Job[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!localStorage.getItem("access")) {
      router.replace("/login");
      return;
    }
    api
      .get<Job[]>("/jobs/match/")
      .then((res) => setJobs(res.data))
      .catch(() =>
        setError("Failed to load matches. Make sure you have an uploaded resume.")
      )
      .finally(() => setLoading(false));
  }, [router]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-2">AI Job Matches</h1>
      <p className="text-sm text-gray-500 mb-6">Ranked by cosine similarity to your resume embedding</p>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {loading ? (
        <p className="text-gray-500">Loading matches...</p>
      ) : jobs.length === 0 ? (
        <p className="text-gray-500">
          No matches found. Upload a resume to see AI-ranked jobs.
        </p>
      ) : (
        <div className="flex flex-col gap-3">
          {jobs.map((job, index) => (
            <div
              key={job.id}
              className="bg-white border border-gray-200 rounded-xl p-5 shadow-sm flex items-start justify-between gap-4"
            >
              <div>
                <span className="text-xs text-gray-400 font-mono">#{index + 1}</span>
                <h2 className="text-base font-semibold text-gray-900">{job.title}</h2>
                <p className="text-sm text-gray-600">{job.company}</p>
                <p className="text-xs text-gray-400">{job.location}</p>
              </div>
              <div className="flex flex-col items-end gap-2 shrink-0">
                <span className="text-xs bg-gray-100 text-gray-600 rounded px-2 py-1">
                  {job.source_platform}
                </span>
                {job.job_url && (
                  <a
                    href={job.job_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-blue-600 hover:underline"
                  >
                    View listing →
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
