# Detection-of-DDOS-Attacks-in-SDN-using-ML
Running the DDOS Attack Prediction:

To run this DDOS attack prediction app, follow these steps:

    Ensure you have all the required files in the same directory:
        Decision Tree.ipynb
        Test.csv
        Train.csv
        ddos.sav
        ddos_app.py
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
        Refer to the "About" page for more info on each input field

Important: Do not close the terminal window running the streamlit command - this will terminate the app.

This DDOS attack prediction app uses a Decision Tree model trained on DDOS network traffic data. The input fields allow you to enter values for various network packet attributes. Once submitted, the app will predict whether a DDOS attack is occurring based on the input values.
