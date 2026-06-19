async function recommendCareer() {
    const skills = document.getElementById("skills").value.trim();
    const education = document.getElementById("education").value;
    const interests = document.getElementById("interests").value.trim();
    const experience = document.getElementById("experience").value;
    const resultBox = document.getElementById("result");

    if (!skills) {
        showError("Please enter your skills.");
        return;
    }

    if (!interests) {
        showError("Please enter your interests.");
        return;
    }

    if (!experience) {
        showError("Please enter your experience.");
        return;
    }

    if (experience < 0 || experience > 30) {
        showError("Experience must be between 0 and 30.");
        return;
    }

    resultBox.style.display = "block";
    resultBox.innerHTML = `
        <h3>⏳ AI is analyzing your profile...</h3>
    `;

    try {
        const response = await fetch("http://127.0.0.1:8000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                skills,
                education,
                interests,
                experience: parseInt(experience)
            })
        });

        if (!response.ok) {
            throw new Error("Server returned invalid response");
        }

        const data = await response.json();

localStorage.setItem("careerResult", JSON.stringify(data));

window.location.href = "results.html";

        let roadmapHTML = "";
data.roadmap.forEach(step => {
    roadmapHTML += `<li>${step}</li>`;
});

        let top3HTML = "";
        data.top_3_recommendations.forEach(item => {
            top3HTML += `<li>${item.career} — ${item.score}%</li>`;
        });

        let skillsHTML = "";
        data.missing_skills.forEach(skill => {
            skillsHTML += `<li>${skill}</li>`;
        });

        localStorage.setItem("careerResult", JSON.stringify(data));
window.location.href = "results.html";

    } catch (error) {
        showError("Unable to connect to backend server.");
    }
}


function showError(message) {
    const resultBox = document.getElementById("result");

    resultBox.style.display = "block";

    resultBox.innerHTML = `
        <h3>Error</h3>
        <p>${message}</p>
    `;
}

async function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    const resultBox = document.getElementById("result");

    if (!fileInput.files.length) {
        showError("Please select a PDF resume.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    resultBox.style.display = "block";
    resultBox.innerHTML = `
        <h3>📄 Uploading and analyzing resume...</h3>
    `;

    try {
        const response = await fetch("http://127.0.0.1:8000/upload_resume", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const data = await response.json();

localStorage.setItem("careerResult", JSON.stringify(data));

window.location.href = "results.html";
        let roadmapHTML = "";
data.roadmap.forEach(step => {
    roadmapHTML += `<li>${step}</li>`;
});

        let top3HTML = "";
        data.top_3_recommendations.forEach(item => {
            top3HTML += `<li>${item.career} — ${item.score}%</li>`;
        });

        let skillsHTML = "";
        data.extracted_skills.forEach(skill => {
            skillsHTML += `<li>${skill}</li>`;
        });

        let missingHTML = "";
        data.missing_skills.forEach(skill => {
            missingHTML += `<li>${skill}</li>`;
        });

        localStorage.setItem("careerResult", JSON.stringify(data));
window.location.href = "results.html";

    } catch (error) {
        showError("Resume upload failed.");
    }
}