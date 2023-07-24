# Detection-of-DDOS-Attacks-in-SDN-using-ML
Running the DDOS Attack Prediction:

To run this DDOS attack prediction app, follow these steps:

    Ensure you have all the required files in the same directory:
        Decision Tree.ipynb
        Test.csv
        Train.csv
        ddos.sav (This is a copy of the locally run ddos.sav file on my pc.)
    Run Decision Tree.ipynb to generate ddos.sav model file
        This Jupyter notebook will train a Decision Tree model and save it to ddos.sav
        Make sure ddos.sav is placed in the required files directory
    Install Streamlit if you don't already have it:
        Open a command prompt/terminal
        Run: pip install streamlit
    Run the Streamlit app:
        In the terminal, navigate to the app directory
        Run: streamlit run ddos_app.py
        This will launch the app in your default web browser
    Use the app:
        On the sidebar, select "DDOS ATTACK PREDICTION"
        Enter values for each of the fields
        Click the "Ddos Result" button to generate a prediction
        To learn more about each input field, click the "About" page

Important: Do not close the terminal window running the streamlit command - this will terminate the app.

This DDOS attack prediction app uses a Decision Tree model trained on DDOS network traffic data. The input fields allow you to enter values for various network packet attributes. Once submitted, the app will predict whether a DDOS attack is occurring based on the input values.
