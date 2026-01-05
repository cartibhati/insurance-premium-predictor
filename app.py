from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.prediction_response import PredictionResponse
from Schema.user_input import UserInput
from Model.predict import predict_output, model, MODEL_VERSION

app = FastAPI(
    title="Insurance Premium Prediction API",
    version=MODEL_VERSION,
    description="ML-powered API to predict insurance premium category",
)


# Human-readable endpoint
@app.get("/")
def home():
    return {
        "message": "Insurance Premium Prediction API"
    }


# Machine-readable health check
# Useful for deployment platforms (AWS, Render, Docker, etc.)
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }


# Prediction endpoint
@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data: UserInput):
    """
    Accepts validated user input and returns
    the predicted insurance premium category.
    """

    # Extract engineered features
    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(
            status_code=200,
            content={
                "Response": prediction
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
