from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app) 

# Load dataset
df = pd.read_csv("C:/Users/HP/Documents/ML and AI/Tesco_ grocery_FAQ'S.csv")

# Preprocess the data
df["Cleaned_questions"] = df["Question"].str.lower()  # Convert questions to lowercase

# Vectorize questions using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Cleaned_questions"])

# Chatbot response function
def get_response(user_query):
    user_query = user_query.lower()
    
    if user_query in ["hello", "hi"]:
        return "Hello! How can I assist you today?"
    if user_query in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    
    # Convert user input to TF-IDF
    user_tfidf = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    best_match_idx = np.argmax(similarities)
    best_match_score = similarities[0, best_match_idx]
    
    if best_match_score < 0.3:
        return "I'm sorry, I didn't understand. Can you rephrase?"
    
    return df.iloc[best_match_idx]["Answer"]

# Flask Routes
@app.route("/")
def home():
    return render_template("chatbot.index.html")  # Load your HTML page

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["message"]
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

