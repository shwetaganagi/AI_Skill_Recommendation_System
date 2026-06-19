KNOWN_SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "numpy",
    "pandas",
    "docker",
    "git",
    "html",
    "css",
    "javascript",
    "react",
    "node js",
    "flask",
    "django",
    "aws",
    "linux",
    "kubernetes",
    "power bi",
    "excel",
    "data analysis",
    "nlp"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills