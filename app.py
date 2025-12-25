from flask import Flask, render_template, request
import pickle
import pandas as pd

# ✅ STEP 1: Create Flask app FIRST
app = Flask(__name__)

# ✅ STEP 2: Load model (optional – not used directly now)
# model = pickle.load(open("model.pkl", "rb"))

# ✅ STEP 3: Static data (must be ABOVE routes)
restaurant_data = {
    "Goa Beaches": ["Fisherman's Wharf", "Britto's", "Souza Lobo"],
    "Taj Mahal": ["Pinch of Spice", "Joney's Place"],
    "Kerala Backwaters": ["Rice Boat", "Villa Maya"],
    "Leh Ladakh": ["Gesmo Restaurant", "Lamayuru Restaurant"]
}

weather_data = {
    "Goa Beaches": "Sunny, 30°C",
    "Taj Mahal": "Clear, 28°C",
    "Kerala Backwaters": "Humid, 29°C",
    "Leh Ladakh": "Cold, 12°C"
}

# ✅ STEP 4: Home route
@app.route('/')
def home():
    return render_template("index.html")

# ✅ STEP 5: Predict route
@app.route('/predict', methods=['POST'])
def predict():
    interest = request.form['interest']
    budget = request.form['budget']
    duration = request.form['duration']

    recommendation_rules = {
        "beach": "Goa Beaches",
        "history": "Taj Mahal",
        "nature": "Kerala Backwaters",
        "adventure": "Leh Ladakh"
    }

    destination_name = recommendation_rules.get(interest, "Goa Beaches")

    restaurants = restaurant_data.get(destination_name, ["Local restaurants available"])
    weather = weather_data.get(destination_name, "Weather data unavailable")

    return render_template(
        "result.html",
        destination=destination_name,
        restaurants=restaurants,
        weather=weather
    )

# ✅ STEP 6: Run app (ALWAYS AT END)
if __name__ == '__main__':
    app.run(debug=True)
