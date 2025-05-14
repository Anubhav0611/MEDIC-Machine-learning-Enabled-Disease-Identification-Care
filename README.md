
# MEDIC 🩺  
**Machine-learning Enabled Disease Identification & Care**

MEDIC is an intelligent web-based disease prediction system that uses machine learning to predict possible diseases based on user-selected symptoms. Built with Django and powered by a trained Random Forest model, MEDIC helps users get preliminary insights before consulting a doctor.

---

## 🔍 Features

- 🌐 Web interface for symptom selection
- 🧠 ML-powered prediction (Random Forest Classifier)
- 📊 Trained on a dataset of 100+ symptoms and diagnoses
- 🔄 Input normalization and vectorization
- 💾 Model saved and loaded using `pickle` or `joblib`
- 📈 Accuracy and classification report on test data

---

## 🏗️ Tech Stack

- **Frontend**: HTML, CSS (basic Django templates)
- **Backend**: Django (Python)
- **Machine Learning**: scikit-learn
- **Model**: Random Forest Classifier
- **Data Handling**: Pandas

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/Anubhav0611/MEDIC-Machine-learning-Enabled-Disease-Identification-Care.git
   cd MEDIC-Machine-learning-Enabled-Disease-Identification-Care
   ```

2. **Set up virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
    ```bash
   pip install -r requirements.txt
   ```

4. **Run Django server**
   ```bash
   python manage.py runserver
   ```

5. **Access in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🧠 Machine Learning Model

- Trained on `Training.csv` dataset
- Features: 100+ symptoms
- Target: Disease prognosis
- Model: RandomForestClassifier (Scikit-learn)
- Accuracy: ~90–95% on test data



---

## 🙋‍♂️ Future Improvements

- Add confidence scores or probabilities
- Improve UI (Bootstrap/React)
- Add login/signup for user history
- Integrate medical advice / disclaimer
- Deploy to cloud (Heroku/Vercel/Render)

---



## 🙌 Acknowledgments

- [scikit-learn](https://scikit-learn.org/)
- [Django](https://www.djangoproject.com/)
- Dataset inspired by disease symptom datasets available in the public domain

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

> 🔗 Made with ❤️ by [Anubhav Shrivastava]
