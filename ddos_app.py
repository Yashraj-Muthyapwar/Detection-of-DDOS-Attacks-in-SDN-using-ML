import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# loading the saved models
ddos_model = pickle.load(open('ddos.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = st.selectbox('DDOS ATTACK PREDICTION using ml', ['Home', 'DDOS ATTACK PREDICTION'])

# DDOS Prediction Page
if (selected == 'Home'):
    st.title('DDOS ATTACK PREDICTION using ml')

# DDOS Prediction Page
if (selected == 'DDOS ATTACK PREDICTION'):
    st.title('DDOS ATTACK PREDICTION ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        id = st.text_input('id', '0')

    with col2:
        duration = st.text_input('duration ', '0')

    with col3:
        protocoltype = st.selectbox('protocoltype', ('tcp', 'udp', 'icmp'))

    # One-hot encode the 'protocoltype' feature
    protocol_encoder = OneHotEncoder(sparse_output=False)
    protocoltype_encoded = protocol_encoder.fit_transform([[protocoltype]])

    with col1:
        service = st.selectbox('service', ('http', 'ftp', 'telnet', 'private', 'other'))

    # One-hot encode the 'service' feature
    service_encoder = OneHotEncoder(sparse_output=False)
    service_encoded = service_encoder.fit_transform([[service]])

    with col2:
        flag = st.selectbox('flag', ('SF', 'S1', 'S2', 'S3', 'OTH', 'REJ', 'RSTO'))

    # One-hot encode the 'flag' feature
    flag_encoder = OneHotEncoder(sparse_output=False)
    flag_encoded = flag_encoder.fit_transform([[flag]])

    with col3:
        srcbytes = st.text_input('srcbytes', '0')

    with col1:
        dstbytes = st.text_input('dstbytes', '0')

    with col2:
        land = st.text_input('land', '0')

    with col3:
        wrongfragment = st.text_input('wrongfragment', '0')

    with col1:
        urgent = st.text_input('urgent', '0')

    with col2:
        hot = st.text_input('hot', '0')

    with col3:
        numfailedlogins = st.text_input('numfailedlogins', '0')

    with col1:
        loggedin = st.text_input('loggedin', '0')

    with col2:
        numcompromised = st.text_input('numcompromised', '0')

    with col3:
        rootshell = st.text_input('rootshell', '0')

    with col1:
        suattempted = st.text_input('suattempted', '0')

    with col2:
        numroot = st.text_input('numroot', '0')

    with col3:
        numfilecreations = st.text_input('numfilecreations', '0')

    with col1:
        numshells = st.text_input('numshells', '0')

    with col2:
        numaccessfiles = st.text_input('numaccessfiles', '0')

    with col3:
        numoutboundcmds = st.text_input('numoutboundcmds', '0')

    with col1:
        ishostlogin = st.text_input('ishostlogin', '0')

    with col2:
        isguestlogin = st.text_input('isguestlogin', '0')

    with col3:
        count = st.text_input('count', '0')

    with col1:
        srvcount = st.text_input('srvcount', '0')

    with col2:
        serrorrate = st.text_input('serrorrate', '0')

    # code for Prediction
    if st.button('Ddos Result'):
        try:
            # Prepare input data with proper type conversion and one-hot encoding
            input_data = np.array([
                float(id),
                float(duration),
                *protocoltype_encoded.flatten(),
                *service_encoded.flatten(),
                *flag_encoded.flatten(),
                float(srcbytes),
                float(dstbytes),
                float(land),
                float(wrongfragment),
                float(urgent),
                float(hot),
                float(numfailedlogins),
                float(loggedin),
                float(numcompromised),
                float(rootshell),
                float(suattempted),
                float(numroot),
                float(numfilecreations),
                float(numshells),
                float(numaccessfiles),
                float(numoutboundcmds),
                float(ishostlogin),
                float(isguestlogin),
                float(count),
                float(srvcount),
                float(serrorrate)
            ]).reshape(1, -1)

            # Predict
            ddos_prediction = ddos_model.predict(input_data)

            if ddos_prediction[0] == 0:
                st.success(f'The output is {ddos_prediction[0]}. Not a DDOS ATTACK')
            else:
                st.warning(f'The output is {ddos_prediction[0]}. It is a DDOS ATTACK')

        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")

# About section
if st.button("About"):
    st.header("DDOS ATTACK PREDICTION ML")
    st.markdown("""
        This web application is designed to predict whether a network connection is classified as a DDOS (Distributed Denial of Service) attack or not using machine learning.

        **Features Used for Prediction:**

        - id: A unique identifier for the network connection.
        - service: The type of network service associated with the connection.
        - dstbytes: Number of data bytes sent to the destination during a network connection.
        - urgent: The urgency of the connection.
        - loggedin: Indicates whether the user is logged in or not.
        - suattempted: Indicates if the superuser access was attempted.
        - numshells: The number of shell prompts used in the connection.
        - ishostlogin: Indicates if the login is from the host.
        - srvcount: The number of services used in the connection.
        - duration: The duration of the connection.
        - flag: The flag associated with the connection.
        - land: Indicates whether the source and destination IP addresses are the same.
        - hot: Indicates if the connection is hot (active) or not.
        - numcompromised: The number of compromised connections.
        - numroot: The number of root accesses.
        - numaccessfiles: The number of accessed files.
        - isguestlogin: Indicates if the login is from a guest.
        - serrorrate: The rate of connection error.
        - protocoltype: The protocol type used in the connection.
        - srcbytes: The number of source bytes in the connection.
        - wrongfragment: Indicates whether there was an incorrect or malformed fragment in the network packet.
        - numfailedlogins: The number of failed login attempts.
        - rootshell: Indicates if the root shell was obtained.
        - numfilecreations: The number of file creations.
        - numoutboundcmds: The number of outbound commands.
        - count: The count of connections.

        The machine learning model used for prediction is a Decision Tree Classifier trained on a labeled dataset.

        **Disclaimer:**

        This application is for educational and demonstration purposes only. The predictions made by the model should not be solely relied upon for critical decision-making regarding network security. It's always recommended to consult with cybersecurity professionals and use multiple security measures to protect your network.

        Built with Streamlit.
    """)