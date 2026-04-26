import type { Metadata } from "next";
import "./styles.css";

export const metadata: Metadata = {
  title: "Sapphire Org Platform",
  description: "Local fallback dashboard for OSINT and crypto signals"
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

