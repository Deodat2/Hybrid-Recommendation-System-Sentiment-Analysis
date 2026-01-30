from fastapi import FastAPI
import joblib
import pandas as pd

# We initialize the application
app = FastAPI()

# --- LOADING DATA ON STARTUP ---
# We load the files created by the Notebook
try:
    predicted_ratings = joblib.load('predicted_ratings.pkl')
    item_sentiment = joblib.load('item_sentiment.pkl')
    print("Models loaded and ready !")
except:
    print("Error: The .pkl files cannot be found. Run the Notebook first !")


# --- YOUR RECOMMENDATION FUNCTION (identical) ---
def get_final_recommendation(user_id, top_n=5):

    if user_id not in predicted_ratings.index:
        return None

    recs = predicted_ratings.loc[user_id].copy()
    for asin in recs.index:
        if asin in item_sentiment:
            recs[asin] += (item_sentiment[asin] * 2)
    return recs.sort_values(ascending=False).head(top_n)

# --- API ROUTES ---
@app.get("/")
def home():
    return {"message": "Welcome to the Luxury Beauty Recommendation API"}


@app.get("/recommend/{user_id}")
def recommend(user_id: str):

    results = get_final_recommendation(user_id)

    if results is None:
        return {"error": "Unknown user"}

    return {
        "user_id": user_id,
        "recommendations": results.to_dict()
    }