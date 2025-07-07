import os
import requests
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Paths
MODEL_PATH = "model/model.h5"
TOKENIZER_PATH = "model/tokenizer.pickle"
DROPBOX_MODEL_URL = "https://www.dropbox.com/scl/fi/4i7txy19stejc2pzn91ok/model.h5?rlkey=vcs5ogp0e6b0thl41ky5nc78c&st=5kdauggt&dl=1"

# Ensure 'model' folder exists
os.makedirs("model", exist_ok=True)

# Download model from Dropbox if not found locally
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Dropbox...")
    response = requests.get(DROPBOX_MODEL_URL)
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)
    print("Model downloaded successfully.")

# Load model and tokenizer
model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)

MAX_SEQUENCE_LENGTH = 500  # should match your training preprocessing

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No input text provided'}), 400

    # Preprocess text
    sequences = tokenizer.texts_to_sequences([text])
    padded_seq = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    # Make prediction
    prediction = model.predict(padded_seq)[0][0]
    label = "FAKE" if prediction > 0.5 else "REAL"
    confidence = float(prediction if label == "FAKE" else 1 - prediction) * 100

    return jsonify({
        "label": label,
        "confidence": f"{confidence:.2f}%"
    })

if __name__ == '__main__':
    app.run(debug=True)
