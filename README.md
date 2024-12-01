# Detection-of-DDOS-Attacks-in-SDN-using-ML
Running the DDOS Attack Prediction:

To run this DDOS attack prediction app, follow these steps:

    Ensure you have all the required files in the same directory:
        XGBoost.ipynb (This is the Jupyter notebook that trains the XGBoost model and saves it as 'ddos.sav').
        Test.csv (Test dataset for prediction)
        Train.csv (Training dataset for model training)
        ddos.sav (This is the saved XGBoost model file generated from training.)
    Run XGBoost_Model.ipynb to generate the ddos.sav model file.
        This Jupyter notebook will train an XGBoost model on the provided network traffic data and save the trained model as ddos.sav.
        Make sure ddos.sav is placed in the required files directory.
    Install Streamlit if you don't already have it:
        Open a command prompt/terminal
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
