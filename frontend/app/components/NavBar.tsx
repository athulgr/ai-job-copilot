"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/jobs", label: "Jobs" },
  { href: "/tracker", label: "Tracker" },
  { href: "/resume", label: "Resume" },
];

export default function NavBar() {
  const pathname = usePathname();
  const router = useRouter();

  if (pathname === "/login") return null;

  function handleLogout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    router.replace("/login");
  }

  return (
    <nav className="bg-white border-b border-gray-200 px-8 py-3 flex items-center gap-6">
      <span className="font-bold text-gray-900 mr-2">Job Copilot</span>
      {NAV_LINKS.map(({ href, label }) => (
        <Link
          key={href}
          href={href}
          className={`text-sm transition-colors ${
            pathname === href
              ? "text-blue-600 font-medium"
              : "text-gray-500 hover:text-gray-900"
          }`}
        >
          {label}
        </Link>
      ))}
      <button
        onClick={handleLogout}
        className="ml-auto text-sm text-gray-400 hover:text-gray-700"
      >
        Sign out
      </button>
    </nav>
  );
}
