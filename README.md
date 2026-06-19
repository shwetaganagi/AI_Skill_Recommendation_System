🚀 AI Skill Recommendation System

An AI-powered career recommendation platform that analyzes a user’s skills, education, interests, experience, and resume to suggest the most suitable career path along with personalized learning roadmaps and skill gap analysis.

⸻

📌 Features

🎯 Career Recommendation

* Predicts the most suitable career domain based on user profile.
* Uses trained Machine Learning models for prediction.

📊 Top 3 Career Matches

* Displays the top three career recommendations with confidence scores.
* Helps users explore alternative career paths.

🧠 Skill Gap Analysis

* Identifies missing skills required for the recommended career.
* Provides actionable insights for improvement.

🗺️ Learning Roadmap

* Generates a structured roadmap to achieve the recommended career goal.
* Suggests technologies and concepts to learn.

📄 Resume Analysis

* Upload PDF resumes.
* Extract skills automatically from resumes.
* Improve recommendation accuracy using resume content.

🌐 Interactive Web Interface

* Modern responsive UI.
* FastAPI backend integration.
* Real-time prediction results.

⸻

🖥️ Application Preview

Career Assessment Dashboard

Recommendation Results

⸻

🏗️ Project Architecture

ML_PROJECT/
│
├── backend/
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── results.html
│   ├── script.js
│   ├── results.js
│   ├── style.css
│   └── results.css
│
├── src/
│   └── models/
│       ├── predict.py
│       ├── train_model.py
│       └── evaluate.py
│
├── resume_parser/
│   ├── parser.py
│   └── skill_extractor.py
│
├── models/
│   ├── random_forest_model.pkl
│   ├── svm_model.pkl
│   ├── logistic_model.pkl
│   ├── neural_network_model.pkl
│   ├── encoder.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── data/
├── notebooks/
├── tests/
└── README.md

⚙️ Tech Stack

Frontend

* HTML5
* CSS3
* JavaScript

Backend

* FastAPI
* Uvicorn

Machine Learning

* Scikit-Learn
* Pandas
* NumPy

Resume Processing

* PDF Parsing
* Skill Extraction

Tools

* Git
* GitHub
* VS Code

⸻

🤖 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Encoding & Scaling
5. Model Training
6. Model Evaluation
7. Career Prediction
8. Recommendation Generation

⸻

📈 Sample Output

Recommended Career

Machine Learning Engineer

Top Career Matches

1. Machine Learning Engineer
2. Data Scientist
3. Backend Developer

Missing Skills

TensorFlow
PyTorch
Deep Learning
NumPy
Machine Learning

⸻

🚀 Installation & Setup

Clone Repository

git clone https://github.com/shwetaganagi/AI_Skill_Recommendation_System.git
cd AI_Skill_Recommendation_System

Create Virtual Environment

python -m venv .venv
source .venv/bin/activate

Install Dependencies

pip install -r backend/requirements.txt

Run FastAPI Server

uvicorn backend.main:app --reload

Open API Documentation

http://127.0.0.1:8000/docs

⸻

🔮 Future Enhancements

* LLM-based Career Mentor
* Job Recommendation Engine
* Industry Trend Analysis
* LinkedIn Profile Integration
* Skill Certification Suggestions
* Personalized Learning Courses

⸻

👩‍💻 Author

Shweta N Ganagi

Computer Science Engineering Student
Bangalore Institute of Technology

GitHub: https://github.com/shwetaganagi

⸻

📄 License

This project is developed for educational and academic purposes.
