```markdown
# 📰 Fake News Detector using LSTM | Deep Learning with Flask UI

This project is a **Fake News Detection System** built using an **LSTM deep learning model** trained on news articles. It uses **Keras with TensorFlow backend** for training and a **Flask web app** for serving predictions. You input a news headline or paragraph, and the model predicts whether it's **real** or **fake**.

---

## 📌 Features

- ✅ Deep learning LSTM-based classifier
- ✅ High accuracy (99%+ on test data)
- ✅ Word2Vec-based embeddings
- ✅ Clean, user-friendly Flask web interface
- ✅ Input custom news and get instant results
- ✅ Fully working local app with UI

---

## 📊 Model Performance

| Metric        | Score |
|---------------|-------|
| Accuracy      | 99.44% |
| Precision     | 0.99  |
| Recall        | 0.99  |
| F1-Score      | 0.99  |

---

## 🧠 Technologies Used

- Python 3.x  
- TensorFlow & Keras  
- Word2Vec (Gensim)  
- Scikit-learn  
- NLTK (text preprocessing)  
- Flask (UI deployment)  
- HTML, CSS, Jinja2 (Frontend)

---

## 📂 Project Structure

```

📁 Fake-News-Detector-LSTM-DeepLearning
│
├── app.py                    # Flask app
├── model.h5                  # Trained LSTM model
├── tokenizer.pickle          # Tokenizer used during training
├── templates/
│   └── index.html            # Frontend HTML file
├── static/
│   └── style.css             # Optional custom CSS
├── requirements.txt          # All dependencies
└── README.md                 # Project documentation

````

---

## 🚀 How to Run Locally

### 🔧 Step 1: Clone the Repository
```bash
git clone https://github.com/mihirdhangdhariya/Fake-News-Detector-LSTM-DeepLearning.git
cd Fake-News-Detector-LSTM-DeepLearning
````

### 🧪 Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/Mac
```

### 📦 Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### 🧠 Step 4: Make Sure These Files Exist

* `model.h5` (trained model)
* `tokenizer.pickle` (trained tokenizer)

(You should have them in the repo. If not, retrain the model or copy them.)

### ▶️ Step 5: Run the Flask App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📷 UI Preview

> *(Add a screenshot here showing your web UI in action)*
> You can take a screenshot of your browser when the app is running and upload it in the repo.

---

## 📌 Example Inputs

* **Real News:**
  *"The Prime Minister held a cabinet meeting today regarding agricultural reform."*

* **Fake News:**
  *"Aliens helped the government construct the new secret underground base."*

---

## 📬 Future Improvements

* Add support for longer news articles
* Use pre-trained BERT embeddings for higher accuracy
* Add user authentication & feedback
* Deploy the app on Render / Hugging Face Spaces

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## 🙌 Author

**Mihir Dhangdhariya**
📬 [GitHub](https://github.com/mihirdhangdhariya)
