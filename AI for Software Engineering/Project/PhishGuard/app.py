from flask import Flask, render_template, request
import joblib

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        email_text = request.form["email"]
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)[0]
        result = "🚨 Phishing Email Detected!" if prediction == 1 else "✅ Safe Email"
        return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)