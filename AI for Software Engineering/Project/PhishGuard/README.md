
🚨 PhishGuard – AI-Powered Phishing Email Detection

PhishGuard is an intelligent machine learning system designed to detect and classify phishing emails with high accuracy.
Built as part of an end-to-end security-focused ML project, it combines data science, cybersecurity best practices, and a Flask web deployment for real-time email scanning.

📌 Project Overview

FeatureDescription🎯 ObjectivePredict whether an email is phishing or legitimate🧠 Model Type(Logistic Regression / Random Forest / SVM)📊 AccuracyXX% (90%)🧾 DatasetPhishing email dataset containing text-based features🌐 Web AppBuilt using Flask, supports real-time input & classification🔐 DomainCybersecurity – Email Threat Detection 

🔍 How It Works

Data Collection & Cleaning

Exploratory Data Analysis (with visualizations)

Feature Engineering (TF-IDF Vectorization)

Model Training & Evaluation

Web Deployment via Flask

Integration-ready for enterprise mail filters

🛠️ Tech Stack

CategoryToolsLanguagesPythonML LibrariesScikit-Learn, NumPy, PandasFeature EngineeringTF-IDF (n-gram based)VisualizationMatplotlibDeploymentFlaskModel Savingjoblib / pickle 

🚀 Installation & Setup

# Clone the repository git clone https://github.com/Zordtech/PLP/PhishGuard.git cd PhishGuard # Install dependencies pip install -r requirements.txt # Start the Flask app python app.py 

Access locally via:
👉 http://127.0.0.1:5000/

📦 Project Structure

PhishGuard/ │ ├── data/ # Dataset(s) ├── notebooks/ # Jupyter workflow ├── models/ # Trained model + TF-IDF vectorizer (.pkl) ├── app.py # Flask web app ├── requirements.txt # Dependencies └── README.md # This file 

🧪 Model Development Steps

Load & Clean Dataset

EDA with visual insights

Feature Extraction using TF-IDF

Model Training & Evaluation

Hyperparameter Tuning

Save model as .pkl

Deploy via Flask

🔒 Security Considerations

✔ Validated against common phishing patterns
✔ Resistant to spam-triggering keywords
✔ Optimized for false-positive minimization
✔ Can be integrated with email gateways & enterprise SIEMs

🧭 Future Improvements

Integration with NLP transformers (BERT)

Real-time threat intelligence feed

Automated email quarantine system

API endpoint for enterprise use

🤝 Contributing

Contributions, improvements, and feature suggestions are welcome!

# Create a new branch git checkout -b feature-name # Commit your changes git commit -m "Added new feature" # Push to your branch git push origin feature-name 

📜 License

This project is licensed under the MIT License – feel free to use and improve it.

💬 Contact / Author

Developer: Zordtech (Dragon)
Email: dragon@zord.tech
LinkedIn: linkedIn.com/in/temidayo-emmanuelle
Project Code Name: Operation SafeZone – Phase 1: PhishGuard

“In cybersecurity, the first line of defense is awareness,
but the most powerful defense is intelligence.”

🔥 PhishGuard your Emails – Because one click can cost everything.


