import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0", // Allow external connections
    port: 5173,
    // Add this proxy configuration
    proxy: {
      // Any request starting with /api will be proxied
      "/api": {
        // Use environment variable for Docker, fallback to localhost for local dev
        target: process.env.VITE_API_URL || "http://localhost:8080",
        changeOrigin: true, // Needed for virtual hosted sites
        // We don't need to rewrite the path, as our gateway expects /api/...
      },
    },
  },
});
