const API_URL = "http://127.0.0.1:8000/analyze_resume_report";
const RESULT_KEY = "resumeAnalysisResult";
const ERROR_KEY = "resumeAnalysisError";

document.addEventListener("DOMContentLoaded", () => {
  const page = document.body.dataset.page;

  if (page === "home") {
    initHomePage();
  } else if (page === "result") {
    initResultPage();
  } else if (page === "error") {
    initErrorPage();
  }

  bindCommonActions();
});

function initHomePage() {
  const form = document.getElementById("analyze-form");
  const loading = document.getElementById("loading-state");
  const submitButton = document.getElementById("analyze-button");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    clearStoredMessages();

    const fileInput = document.getElementById("resume-file");
    const descriptionInput = document.getElementById("job-description");
    const file = fileInput.files[0];
    const jobDescription = descriptionInput.value.trim();

    if (!file || !jobDescription) {
      setErrorAndRedirect("Please upload a resume and provide a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    setLoadingState(true, loading, submitButton);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        body: formData
      });

      let payload = null;
      try {
        payload = await response.json();
      } catch (parseError) {
        payload = null;
      }

      if (!response.ok) {
        const message = getErrorMessage(payload, response.status);
        setErrorAndRedirect(message);
        return;
      }

      sessionStorage.setItem(RESULT_KEY, JSON.stringify(payload));
      window.location.href = "results.html";
    } catch (error) {
      setErrorAndRedirect("Could not reach API server. Please verify FastAPI is running on localhost:8000.");
    } finally {
      setLoadingState(false, loading, submitButton);
    }
  });
}

function initResultPage() {
  const raw = sessionStorage.getItem(RESULT_KEY);
  if (!raw) {
    setErrorAndRedirect("No analysis data found. Please submit a resume from the home page.");
    return;
  }

  let result;
  try {
    result = JSON.parse(raw);
  } catch (error) {
    setErrorAndRedirect("Invalid analysis data found. Please run the analysis again.");
    return;
  }

  setText("candidate-name", result.candidate_name || "N/A");
  setText("match-score", formatScore(result.match_score));
  setText("weighted-score", formatScore(result.weighted_match_score));
  setMatchLevel(result.match_level || result.summary || "N/A");
  setList("matched-skills", result.matched_skills || [], "No matched skills found.");
  setList("missing-skills", result.missing_skills || [], "No missing skills found.");
  setText("summary-text", result.summary || "No summary available.");
  setBulletList("improvements-list", result.top_improvements, "No improvements available.");
  setBulletList("category-feedback-list", result.category_feedback, "No category feedback available.");
}

function initErrorPage() {
  const message = sessionStorage.getItem(ERROR_KEY) || "An unexpected error occurred.";
  setText("error-message-text", message);
}

function bindCommonActions() {
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => {
      const action = button.dataset.action;

      if (action === "home" || action === "reset") {
        clearStoredMessages();
        window.location.href = "index.html";
      }

      if (action === "another-job") {
        sessionStorage.removeItem(ERROR_KEY);
        window.location.href = "index.html";
      }
    });
  });
}

function setMatchLevel(rawLevel) {
  const element = document.getElementById("match-level");
  if (!element) {
    return;
  }

  const level = String(rawLevel).toLowerCase();
  element.classList.remove("match-low", "match-moderate", "match-strong");

  if (level.includes("strong")) {
    element.classList.add("match-strong");
    element.textContent = "Strong";
    return;
  }

  if (level.includes("moderate")) {
    element.classList.add("match-moderate");
    element.textContent = "Moderate";
    return;
  }

  if (level.includes("low")) {
    element.classList.add("match-low");
    element.textContent = "Low";
    return;
  }

  element.textContent = rawLevel || "N/A";
}

function setLoadingState(isLoading, loadingElement, submitButton) {
  loadingElement.classList.toggle("hidden", !isLoading);
  submitButton.disabled = isLoading;
  submitButton.textContent = isLoading ? "Analyzing..." : "Analyze";
}

function setErrorAndRedirect(message) {
  sessionStorage.setItem(ERROR_KEY, message);
  sessionStorage.removeItem(RESULT_KEY);
  window.location.href = "error.html";
}

function clearStoredMessages() {
  sessionStorage.removeItem(ERROR_KEY);
  sessionStorage.removeItem(RESULT_KEY);
}

function getErrorMessage(payload, status) {
  if (payload && typeof payload.detail === "string" && payload.detail.trim() !== "") {
    return payload.detail;
  }

  if (payload && typeof payload.message === "string" && payload.message.trim() !== "") {
    return payload.message;
  }

  return `Request failed with status ${status}.`;
}

function setText(id, value) {
  const element = document.getElementById(id);
  if (element) {
    element.textContent = value;
  }
}

function setList(id, items, emptyMessage) {
  const element = document.getElementById(id);
  if (!element) {
    return;
  }

  element.innerHTML = "";
  if (!Array.isArray(items) || items.length === 0) {
    const emptyItem = document.createElement("li");
    emptyItem.textContent = emptyMessage;
    element.appendChild(emptyItem);
    return;
  }

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    element.appendChild(li);
  });
}

function setBulletList(id, textValue, emptyMessage) {
  const element = document.getElementById(id);
  if (!element) {
    return;
  }

  element.innerHTML = "";
  const parsedItems = splitFeedbackText(textValue);

  if (parsedItems.length === 0) {
    const li = document.createElement("li");
    li.textContent = emptyMessage;
    element.appendChild(li);
    return;
  }

  parsedItems.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    element.appendChild(li);
  });
}

function splitFeedbackText(value) {
  if (!value || typeof value !== "string") {
    return [];
  }

  return value
    .split(/[\n;.]+/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

function formatScore(score) {
  const numeric = Number(score);
  if (Number.isFinite(numeric)) {
    return `${numeric.toFixed(2)}%`;
  }
  return "N/A";
}
