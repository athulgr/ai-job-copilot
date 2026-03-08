"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/lib/api";

type ApplicationStatus = "pending" | "applied" | "interview" | "offer" | "rejected";

interface Application {
  id: number;
  job: number;
  resume: number | null;
  status: ApplicationStatus;
  cover_letter: string;
  notes: string;
  applied_at: string | null;
  created_at: string;
}

const NEXT_STATUSES: Record<ApplicationStatus, ApplicationStatus[]> = {
  pending: ["applied"],
  applied: ["interview", "rejected"],
  interview: ["offer", "rejected"],
  offer: [],
  rejected: [],
};

const STATUS_COLORS: Record<ApplicationStatus, string> = {
  pending: "bg-yellow-100 text-yellow-800",
  applied: "bg-blue-100 text-blue-800",
  interview: "bg-purple-100 text-purple-800",
  offer: "bg-green-100 text-green-800",
  rejected: "bg-red-100 text-red-800",
};

export default function TrackerPage() {
  const router = useRouter();
  const [applications, setApplications] = useState<Application[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!localStorage.getItem("access")) {
      router.replace("/login");
      return;
    }
    api
      .get<Application[]>("/applications/")
      .then((res) => setApplications(res.data))
      .catch(() => setError("Failed to load applications."))
      .finally(() => setLoading(false));
  }, [router]);

  async function advance(id: number, newStatus: ApplicationStatus) {
    try {
      const res = await api.patch<Application>(`/applications/${id}/`, {
        status: newStatus,
      });
      setApplications((prev) =>
        prev.map((app) => (app.id === id ? res.data : app))
      );
    } catch {
      setError("Failed to update status.");
    }
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Application Tracker</h1>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {loading ? (
        <p className="text-gray-500">Loading...</p>
      ) : applications.length === 0 ? (
        <p className="text-gray-500">No applications yet.</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full text-sm border-collapse">
            <thead>
              <tr className="text-left border-b border-gray-200">
                <th className="py-3 pr-6 font-medium text-gray-600">ID</th>
                <th className="py-3 pr-6 font-medium text-gray-600">Job</th>
                <th className="py-3 pr-6 font-medium text-gray-600">Status</th>
                <th className="py-3 pr-6 font-medium text-gray-600">Applied At</th>
                <th className="py-3 font-medium text-gray-600">Advance</th>
              </tr>
            </thead>
            <tbody>
              {applications.map((app) => (
                <tr key={app.id} className="border-b border-gray-100 hover:bg-gray-50">
                  <td className="py-3 pr-6 text-gray-400 font-mono">{app.id}</td>
                  <td className="py-3 pr-6 text-gray-800">Job #{app.job}</td>
                  <td className="py-3 pr-6">
                    <span
                      className={`rounded px-2 py-1 text-xs font-medium ${STATUS_COLORS[app.status]}`}
                    >
                      {app.status}
                    </span>
                  </td>
                  <td className="py-3 pr-6 text-gray-500">
                    {app.applied_at
                      ? new Date(app.applied_at).toLocaleDateString()
                      : "—"}
                  </td>
                  <td className="py-3">
                    <div className="flex gap-2">
                      {NEXT_STATUSES[app.status].map((next) => (
                        <button
                          key={next}
                          onClick={() => advance(app.id, next)}
                          className="text-xs bg-gray-800 text-white rounded px-2 py-1 hover:bg-gray-700 transition-colors"
                        >
                          → {next}
                        </button>
                      ))}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
