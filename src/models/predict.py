import pandas as pd
import joblib
from src.config import career_profiles, career_roadmaps

# Load saved model artifacts
model_pipeline = joblib.load("models/neural_network_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

def generate_roadmap(career):
    return career_roadmaps.get(
        career,
        ["No roadmap available for this career yet."]
    )

def recommend_career(skills, education, interests, experience):
    """
    Predict career recommendation based on user profile
    """

    # Create dataframe from user input
    user_df = pd.DataFrame([{
        "skills": skills,
        "education": education,
        "interests": interests,
        "experience": experience
    }])

    # Get prediction probabilities
    probabilities = model_pipeline.predict_proba(user_df)

    # Pair career labels with probabilities
    career_probabilities = list(
        zip(label_encoder.classes_, probabilities[0])
    )

    # Sort descending by probability
    career_probabilities = sorted(
        career_probabilities,
        key=lambda x: x[1],
        reverse=True
    )

    # Top 3 recommendations
    top_3 = career_probabilities[:3]

    # Best recommendation
    top_career = top_3[0][0]

    # Ideal skills for recommended career
    ideal_skills = set(
        skill.lower()
        for skill in career_profiles[top_career]["skills"]
    )

    # User skills
    user_skills = set(
        skill.strip().lower()
        for skill in skills.split(",")
    )

    # Skill gap analysis
    missing_skills = list(ideal_skills - user_skills)

    # Format top 3 output
    formatted_top_3 = [
        {
            "career": career,
            "score": round(score * 100, 2)
        }
        for career, score in top_3
    ]

    roadmap = generate_roadmap(top_career)

    return {
    "recommended_career": top_career,
    "top_3_recommendations": formatted_top_3,
    "missing_skills": missing_skills,
    "roadmap": roadmap
    }