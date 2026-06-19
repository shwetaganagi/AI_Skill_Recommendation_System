from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import UserInput
from src.models.predict import recommend_career

from resume_parser.parser import extract_text_from_pdf
from resume_parser.skill_extractor import extract_skills

import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Career Recommendation API is running"
    }


@app.post("/recommend")
def recommend(user: UserInput):
    return recommend_career(
        user.skills,
        user.education,
        user.interests,
        user.experience
    )
@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(temp_path)

    skills = extract_skills(text)

    os.remove(temp_path)

    if not skills:
        return {
            "error": "No recognizable skills found in resume"
        }

    skills_string = ", ".join(skills)

    result = recommend_career(
        skills=skills_string,
        education="BTech CSE",
        interests="technology",
        experience=1
    )

    result["extracted_skills"] = skills

    return result