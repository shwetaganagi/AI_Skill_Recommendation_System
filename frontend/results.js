window.onload = function () {
    const data = JSON.parse(localStorage.getItem("careerResult"));
    const resultsContent = document.getElementById("resultsContent");

    if (!data) {
        resultsContent.innerHTML = "<h2>No results found.</h2>";
        return;
    }

    // TOP 3 RECOMMENDATIONS
    let top3HTML = "";

if (data.top_3_recommendations) {
    data.top_3_recommendations.forEach(item => {
        let careerName;
        let score;

        if (Array.isArray(item)) {
            careerName = item[0];
            score = item[1];
        } else {
            careerName = item.career;
            score = item.score;
        }

        top3HTML += `
            <div class="card">
                <h3>${careerName}</h3>
                <p>${score}%</p>
            </div>
        `;
    });
}

    // MISSING SKILLS
    let missingHTML = "";
    for (const skill of data.missing_skills || []) {
        missingHTML += `<span class="badge">${skill}</span>`;
    }

    // ROADMAP
    let roadmapHTML = "";
    for (const step of data.roadmap || []) {
        roadmapHTML += `<li>${step}</li>`;
    }

    // EXTRACTED SKILLS (resume upload case)
    let extractedSkillsHTML = "";
    if (data.extracted_skills) {
        for (const skill of data.extracted_skills) {
            extractedSkillsHTML += `<span class="badge">${skill}</span>`;
        }
    }

    resultsContent.innerHTML = `
        <div class="hero-card">
            <h2>🎯 Recommended Career</h2>
            <p class="career-title">${data.recommended_career}</p>
        </div>

        ${extractedSkillsHTML ? `
        <section>
            <h2>📄 Extracted Skills</h2>
            <div>${extractedSkillsHTML}</div>
        </section>
        ` : ""}

        <section>
            <h2>📈 Top 3 Recommendations</h2>
            <div class="card-grid">
                ${top3HTML}
            </div>
        </section>

        <section>
            <h2>🛠 Missing Skills</h2>
            <div>${missingHTML}</div>
        </section>

        <section>
            <h2>🗺 Learning Roadmap</h2>
            <ol>${roadmapHTML}</ol>
        </section>
    `;
};

function goBack() {
    window.location.href = "index.html";
}