"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/lib/api";

interface DashboardSummary {
  total_applications: number;
  pending: number;
  applied: number;
  interview: number;
  offer: number;
  rejected: number;
}

const STAT_CARDS: {
  key: keyof DashboardSummary;
  label: string;
  color: string;
}[] = [
  { key: "total_applications", label: "Total", color: "bg-blue-100 text-blue-800" },
  { key: "pending", label: "Pending", color: "bg-yellow-100 text-yellow-800" },
  { key: "applied", label: "Applied", color: "bg-indigo-100 text-indigo-800" },
  { key: "interview", label: "Interview", color: "bg-purple-100 text-purple-800" },
  { key: "offer", label: "Offer", color: "bg-green-100 text-green-800" },
  { key: "rejected", label: "Rejected", color: "bg-red-100 text-red-800" },
];

export default function DashboardPage() {
  const router = useRouter();
  const [summary, setSummary] = useState<DashboardSummary | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!localStorage.getItem("access")) {
      router.replace("/login");
      return;
    }
    api
      .get<DashboardSummary>("/dashboard/")
      .then((res) => setSummary(res.data))
      .catch(() => setError("Failed to load dashboard."));
  }, [router]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Dashboard</h1>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {!summary ? (
        <p className="text-gray-500">Loading...</p>
      ) : (
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {STAT_CARDS.map(({ key, label, color }) => (
            <div key={key} className={`rounded-xl p-6 ${color}`}>
              <p className="text-sm font-medium">{label}</p>
              <p className="text-3xl font-bold mt-1">{summary[key]}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
