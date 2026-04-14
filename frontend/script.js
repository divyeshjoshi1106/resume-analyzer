document.getElementById("uploadForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const fileInput = document.getElementById("file");
    const jobDesc = document.getElementById("job_description").value;

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    formData.append("job_description", jobDesc);

    const response = await fetch("http://127.0.0.1:8000/analyze_resume_report", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    displayResult(data);
});

function displayResult(data) {
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = `
        <h2>${data.candidate_name}</h2>
        <p><strong>Match Level:</strong> ${data.match_level}</p>
        <p><strong>Match Score:</strong> ${data.match_score}</p>
        <p><strong>Weighted Score:</strong> ${data.weighted_match_score}</p>

        <h3>Matched Skills</h3>
        <p>${data.matched_skills.join(", ")}</p>

        <h3>Missing Skills</h3>
        <p>${data.missing_skills.join(", ")}</p>

        <h3>Summary</h3>
        <p>${data.summary}</p>

        <h3>Improvements</h3>
        <p>${data.top_improvements}</p>

        <h3>Category Feedback</h3>
        <p>${data.category_feedback}</p>
    `;
}