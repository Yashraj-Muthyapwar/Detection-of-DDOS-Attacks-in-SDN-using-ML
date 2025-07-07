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

# 🚀 How to Run the DDoS Attack Prediction System
Running the DDOS Attack Prediction:

To run this DDOS attack prediction app, follow these steps:

    Ensure you have all the required files in the same directory:
        XGBoost.ipynb (This is the Jupyter notebook that trains the XGBoost model and saves it as 'ddos.sav').
        Test.csv (Test dataset for prediction)
        Train.csv (Training dataset for model training)
        ddos.sav (This is the saved XGBoost model file generated from training.)
        requirements.txt (File that contains the necessary dependencies for the app)
    Install the required dependencies:
        You can install all the necessary Python packages by running the following command in your terminal:
        Run: pip install -r requirements.txt
        This will install all the libraries listed in the requirements.txt file, including NumPy, pandas, scikit-learn, XGBoost, Streamlit, and others.
    Run XGBoost_Model.ipynb to generate the ddos.sav model file.
        This Jupyter notebook will train an XGBoost model on the provided network traffic data and save the trained model as ddos.sav.
        Make sure ddos.sav is placed in the required files directory.
    Install Streamlit (Optional):
        Streamlit is included in the requirements.txt file. If you have already installed the dependencies using the previous step, you do not need to install Streamlit separately.
        However, if you prefer to install it manually, you can run the following command:
        Run: pip install streamlit
    Run the Streamlit app:
        In the terminal, navigate to the app directory
        Run: streamlit run ddos_app.py
        This will launch the app in your default web browser
    Use the app:
        On the sidebar, select "DDoS ATTACK PREDICTION".
        Enter values for each of the fields related to network traffic features.
        Click the "DDoS Result" button to generate a prediction of whether a DDoS attack is occurring based on the input values.
        To learn more about each input field, click the "About" page.
        
Important: Do not close the terminal window running the streamlit command - this will terminate the app.

This DDoS attack prediction app uses an XGBoost model trained on DDoS network traffic data. The input fields allow you to provide various network packet attributes. Once the data is entered, the app will predict whether a DDoS attack is happening based on the input features.
