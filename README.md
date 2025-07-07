# 📰 Fake News Detector using LSTM | Deep Learning with Flask UI

A **Fake News Detection System** built using an **LSTM deep learning model** trained on real-world news articles. The system predicts whether a given news snippet is **real** or **fake**.

🔍 Powered by **Keras + TensorFlow**, and deployed via a sleek **Flask web UI**.

---

 ✅ Features

- 🧠 Deep learning model using LSTM
- 📈 99%+ accuracy on test data
- 🧾 Word2Vec-based embeddings
- 🌐 Flask-based web interface
- 💬 Instant prediction on user input
- 🖥️ Simple, clean, and responsive UI

---

 📊 Model Performance

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 99.44% |
| Precision | 0.99   |
| Recall    | 0.99   |
| F1-Score  | 0.99   |

---

 🧠 Tech Stack

- *Language*: Python 3.x  
- *Libraries*: TensorFlow, Keras, Scikit-learn, NLTK, Gensim (Word2Vec)  
- *Web Framework*: Flask  
- *Frontend*: HTML, CSS, Jinja2  
- *Deployment*: Localhost / Render (optional)

```


 📁 Project Structure
```


📦 Fake-News-Detector-LSTM-DeepLearning
│
├── app.py                  # Flask application
├── model/
│   ├── model.h5            # Trained LSTM model
│   └── tokenizer.pickle    # Tokenizer used during training
├── templates/
│   └── index.html          # Web UI template
├── static/
│   └── style.css           # Optional custom styling
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation

````

---

 🚀 Getting Started

# 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/mihirdhangdhariya/Fake-News-Detector-LSTM-DeepLearning.git
cd Fake-News-Detector-LSTM-DeepLearning
````

# 🧪 Step 2: Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

# 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

# 🧠 Step 4: Verify Required Files

Make sure the following files are present:

* `model/model.h5`
* `model/tokenizer.pickle`

> If not, retrain the model or download from release/backup if available.

# ▶️ Step 5: Run the App

```bash
python app.py
```

Open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

 🖼️ UI Preview

> *(Insert a screenshot here showing the UI in action — like entering a headline and getting a result)*
> You can upload a screenshot named `screenshot.png` and embed it like below:

```markdown
![UI Screenshot](screenshot.png)
```

---

 📝 Example Predictions

**✅ Real News:**

> “The Prime Minister held a cabinet meeting today regarding agricultural reforms.”

**❌ Fake News:**

> “Aliens helped the government construct the new secret underground base.”

---

 🌟 Future Improvements

* Support full-length news articles
* Integrate pre-trained BERT/DistilBERT for higher accuracy
* Add feedback system for improving predictions
* Deploy on Hugging Face Spaces or Render
* Add API endpoint for integration with other apps

---

 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).


 🙋‍♂️ Author

**Mihir Dhangdhariya**
🔗 [GitHub Profile](https://github.com/mihirdhangdhariya)
