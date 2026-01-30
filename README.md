# 🌟 Hybrid Recommendation System & Sentiment Analysis

This project is a personalized recommendation engine for Luxury Beauty products (E-commerce). It demonstrates the ability to combine behavioral data (user ratings) with semantic analysis of textual reviews to deliver highly accurate suggestions.

## 🚀 Key Features
- **Sentiment Analysis (NLP)**: Leverages `TextBlob` to extract polarity scores from customer reviews.
- **Recommendation Engine**: Implements Non-negative Matrix Factorization (NMF) using `Scikit-Learn` to predict user preferences.
- **Hybrid Scoring**: Dynamically adjusts AI-predicted ratings based on real-time sentiment analysis (bonus/penalty system).
- **Real-Time API**: High-performance web interface built with `FastAPI` to serve recommendations instantly.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Data Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn (NMF)
- **NLP**: TextBlob, Regular Expressions (re)
- **Backend**: FastAPI, Uvicorn
- **DevOps**: Docker (Deployment ready)

## 📁 Project Structure
- `Exploration_Cleaning.ipynb`: Exploratory Data Analysis (EDA), text preprocessing, and model training.
- `main.py`: Main FastAPI application script.
- `predicted_ratings.pkl`: Serialized matrix of predicted scores.
- `item_sentiment.pkl`: Serialized average sentiment scores per product.
- `requirements.txt`: List of required Python dependencies.

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone <your-github-url>
cd <project-folder-name>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn main:app --reload
```
The API will be live at: http://127.0.0.1:8000

## API Endpoints
- `GET /` : Health check / API status.
- `GET /recommend/{user_id}` : Returns the top 5 adjusted product recommendations for a specific user.