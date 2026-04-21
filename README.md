# 🌱 Cristagro

Cristagro is a machine learning project that predicts crop yield based on climate and environmental factors, providing insights for agricultural decision-making.

## 📌 Overview

Cristagro is a crop yield prediction system built with Python, machine learning, and Streamlit.  
It estimates agricultural productivity using variables such as:

- crop type
- temperature
- rainfall
- soil type
- irrigation

The project was developed as a portfolio project to demonstrate skills in data analysis, machine learning, model deployment, and interactive app development.

---

## 🚀 Features

- Crop yield prediction
- Interactive Streamlit app
- Model training with Random Forest Regressor
- Simple result interpretation
- Simulated agricultural dataset
- Clean project structure for future expansion

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```text
Cristagro/
├── app/
│   └── app.py
├── data/
│   └── raw/
│       └── dados.csv
├── models/
│   ├── model.pkl
│   └── columns.pkl
├── notebooks/
│   └── eda.ipynb
├── src/
├── .gitignore
├── README.md
├── requirements.txt
└── main.py

---

## ▶️ How to Run

Clone the repository:

git clone https://github.com/SEU-USUARIO/Cristagro.git

Go to the folder:

cd Cristagro

Create virtual environment:

py -m venv .venv

Activate environment (PowerShell):

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the app:

py -m streamlit run app/app.py

---

## 📊 Model

- Model: Random Forest Regressor  
- Dataset: simulated (40 rows)  
- Target: produtividade  

---

## 📈 Status

- Dataset created
- Model trained
- App working
- Prediction interpretation added

---

## 🔮 Future Improvements

- Risk analysis
- Better UI
- Scenario simulation
- Real data integration

---

## 👩‍💻 Author

Portfolio project built with Python and Machine Learning.