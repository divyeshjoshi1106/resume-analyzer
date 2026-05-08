const IS_LOCAL =
  window.location.hostname === "localhost" ||
  window.location.hostname === "127.0.0.1";

const CONFIG = {
  API_BASE_URL: IS_LOCAL
    ? "http://127.0.0.1:8000"
    : "https://resume-analyzer-d8ju.onrender.com",

  ENDPOINTS: {
    ANALYZE: "/analyze_resume_report"
  }
};