from flask import Flask, render_template, request
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the model and tokenizer
model = load_model("model/model.h5")
with open("model/tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

maxlen = 500  # Adjust if your model used a different maxlen

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        text = request.form["news"]
        sequence = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(sequence, maxlen=maxlen)
        result = model.predict(padded)[0][0]
        prediction = "Real" if result > 0.5 else "Fake"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
