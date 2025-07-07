from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
import requests
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Constants
MODEL_PATH = "model/model.h5"
TOKENIZER_PATH = "model/tokenizer.pickle"
DROPBOX_MODEL_URL = "https://www.dropbox.com/scl/fi/4i7txy19stejc2pzn91ok/model.h5?rlkey=vcs5ogp0e6b0thl41ky5nc78c&st=5kdauggt&dl=1"

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Download model if it doesn't exist
if not os.path.exists(MODEL_PATH):
    print("🔄 Downloading model from Dropbox...")
    response = requests.get(DROPBOX_MODEL_URL, allow_redirects=True)
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)
    print("✅ Model downloaded successfully.")

# Load model and tokenizer
model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# Set max length (must match training)
maxlen = 500

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["news"]
        sequence = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(sequence, maxlen=maxlen)
        prediction_score = model.predict(padded)[0][0]
        label = "Real" if prediction_score > 0.5 else "Fake"
        confidence = float(prediction_score if prediction_score > 0.5 else 1 - prediction_score)
        confidence_percent = round(confidence * 100, 2)

        return render_template("index.html",
                               prediction=label,
                               confidence=confidence_percent,
                               user_input=text)
    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)