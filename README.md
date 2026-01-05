# Insurance Premium Predictor

An end-to-end **Machine Learning–powered Insurance Premium Predictor** that classifies users into premium categories based on demographic and lifestyle attributes.  
The project exposes a **FastAPI-based REST API** and is designed with a clean, modular architecture suitable for real-world deployment.

---

## 📌 Problem Statement

Insurance companies determine premium categories by evaluating multiple factors such as age, income, body metrics, smoking habits, city, and occupation.  
Manual evaluation of these parameters is time-consuming and inconsistent.

This project automates the process by using a trained Machine Learning model to **predict insurance premium categories**, enabling faster, scalable, and data-driven decisions.

---

## 🚀 Features

- Predicts insurance premium category from user details
- RESTful API built using **FastAPI**
- Input validation using **Pydantic schemas**
- Modular and scalable project structure
- Docker support for containerized deployment
- Easily extendable for production use

---

## 🧠 Tech Stack

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **API Validation:** Pydantic  
- **Containerization:** Docker  

---

## 🏗 Project Architecture & Flow

1. User sends insurance-related data via API request
2. Request is validated using Pydantic schemas
3. Validated data is preprocessed
4. Trained ML model predicts the premium category
5. Prediction is returned as a JSON response

---

## 📂 Project Structure
```
insurance-premium-predictor/
│
├── app.py # Main FastAPI application
│
├── Model/ # Trained ML model and related artifacts
│ └── model.pkl
│
├── Schema/ # Pydantic schemas for request & response validation
│ └── insurance_schema.py
│
├── config/ # Configuration and constants
│ └── settings.py
│
├── Dockerfile # Docker configuration for containerization
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation


---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/insurance-premium-predictor.git
cd insurance-premium-predictor
