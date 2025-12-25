from flask import Flask, render_template, request
import os

# Create Flask app
app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Prediction / Recommendation page
@app.route("/predict", methods=["POST"])
def predict():
    # Get user input from form
    interest = request.form.get("interest")

    # Rule-based recommendation logic
    if interest == "beach":
        destination = "Goa Beaches"
    elif interest == "history":
        destination = "Taj Mahal"
    elif interest == "nature":
        destination = "Kerala Backwaters"
    elif interest == "adventure":
        destination = "Leh Ladakh"
    else:
        destination = "Goa Beaches"

    return render_template("result.html", destination=destination)


# IMPORTANT: Required for Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
