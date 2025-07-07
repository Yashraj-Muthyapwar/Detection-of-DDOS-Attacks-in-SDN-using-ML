<h1 align="center">DETECTION-OF-DDOS-ATTACKS-IN-SDN-USING-ML</h1>

<p align="center"><i>Machine Learning-based system for predicting DDoS attacks in Software Defined Networks (SDN)</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/XGBoost-FF6600?logo=xgboost&logoColor=white" alt="XGBoost">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Numpy-013243?logo=numpy&logoColor=white" alt="Numpy">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-3C4C7E?logo=seaborn&logoColor=white" alt="Seaborn">
</p>

---

# 🚨 DDoS Attack Detection in SDN using ML

This project implements a predictive system for detecting Distributed Denial-of-Service (DDoS) attacks in Software Defined Networks (SDN) using an XGBoost machine learning model, with an interactive web application built using Streamlit.

## 📖 Overview

Leverages machine learning to analyze network traffic features and predict potential DDoS attacks in real time. The solution combines a trained XGBoost model with an interactive Streamlit interface for user-friendly predictions.

---

## 🚀 How to Run the DDoS Attack Prediction System
### 1️⃣ Project Requirements:
Ensure the following files are present in the same directory:
```
├── XGBoost_Model.ipynb      # Notebook to train and generate ddos.sav model
├── Train.csv                # Training dataset
├── Test.csv                 # Test dataset
├── ddos.sav                 # Saved trained XGBoost model file
├── ddos_app.py              # Streamlit web application
├── requirements.txt         # List of project dependencies
```

### 2️⃣ Install Dependencies:
```bash
pip install -r requirements.txt
```
This will install all the libraries listed in the requirements.txt file, including NumPy, pandas, scikit-learn, XGBoost, Streamlit, etc.

### 3️⃣ Train the XGBoost Model (Optional if ddos.sav exists):
Run the notebook:
```bash
XGBoost_Model.ipynb
```
Generates and saves `ddos.sav` (pre-trained model) based on network traffic data.

### 4️⃣ Launch the Streamlit Web App:
```bash
streamlit run ddos_app.py
```
Access the app via your default web browser.

### 5️⃣ Using the App:
- Navigate to **"DDoS ATTACK PREDICTION"** in the sidebar.
- Enter values for network traffic features.
- Click **"DDoS Result"** to predict if a DDoS attack is happening.
- Visit the **"About"** section for feature descriptions.

⚠️ Keep the terminal running Streamlit open during use.

## 🛡 Key Features:
- ML-powered detection of DDoS attacks in SDN environments.
- Uses XGBoost, a highly efficient gradient boosting algorithm.
- User-friendly web interface built with Streamlit.
- Real-time predictions based on customizable traffic attributes.

## 📬 Feedback:
If you find this repository helpful, please consider giving it a ⭐. Thanks!

---
Contributions welcome. Built with ❤️ for securing SDN networks against evolving DDoS threats.
