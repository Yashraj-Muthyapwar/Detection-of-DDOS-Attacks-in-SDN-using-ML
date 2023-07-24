import pickle
import streamlit as st
from sklearn.preprocessing import OneHotEncoder

# loading the saved models

ddos_model = pickle.load(open('ddos.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    # With this code
    selected = st.selectbox('DDOS ATTACK PREDICTION using ml', ['Home', 'DDOS ATTACK PREDICTION'])


# DDOS Prediction Page
if (selected == 'Home'):
    # page title
    st.title('DDOS ATTACK PREDICTION using ml')

# DDOS Prediction Page
if (selected == 'DDOS ATTACK PREDICTION'):

    # page title
    st.title('DDOS ATTACK PREDICTION ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        id = st.text_input('id')

    with col2:
        duration = st.text_input('duration ')

    with col3:
        protocoltype = st.selectbox('protocoltype', ('tcp', 'udp', 'icmp'))

    # One-hot encode the 'protocoltype' feature
    enc = OneHotEncoder(sparse=False)
    protocoltype_encoded = enc.fit_transform([[protocoltype]])

    # Flatten the one-hot encoded feature
    protocoltype_encoded = protocoltype_encoded.flatten()

    with col1:
        service = st.selectbox('service', ('http', 'ftp', 'telnet', 'private', 'other'))

    # One-hot encode the 'flag' feature
    enc = OneHotEncoder(sparse=False)
    service_encoded = enc.fit_transform([[service]])

    # Flatten the one-hot encoded feature
    service_encoded = service_encoded.flatten()

    with col2:
        flag = st.selectbox('flag', ('SF', 'S1', 'S2', 'S3', 'OTH', 'REJ', 'RSTO'))

    # One-hot encode the 'flag' feature
    enc = OneHotEncoder(sparse=False)
    flag_encoded = enc.fit_transform([[flag]])

    # Flatten the one-hot encoded feature
    flag_encoded = flag_encoded.flatten()

    with col3:
        srcbytes = st.text_input('  srcbytes	')

    with col1:
        dstbytes = st.text_input('dstbytes	')

    with col2:
        land = st.text_input('land')

    with col3:
        wrongfragment = st.text_input('wrongfragment')

    with col1:
        urgent = st.text_input('urgent')

    with col2:
        hot = st.text_input('hot')

    with col3:
        numfailedlogins = st.text_input('numfailedlogins')

    with col1:
        loggedin = st.text_input('loggedin')

    with col2:
        numcompromised = st.text_input('numcompromised')

    with col3:
        rootshell = st.text_input('rootshell')

    with col1:
        suattempted = st.text_input('suattempted')

    with col2:
        numroot = st.text_input('numroot')

    with col3:
        numfilecreations = st.text_input('numfilecreations')

    with col1:
        numshells = st.text_input('numshells')

    with col2:
        numaccessfiles = st.text_input('numaccessfiles')

    with col3:
        numoutboundcmds = st.text_input('numoutboundcmds')

    with col1:
        ishostlogin = st.text_input('ishostlogin')

    with col2:
        isguestlogin = st.text_input('isguestlogin')

    with col3:
        count = st.text_input('count')

    with col1:
        srvcount = st.text_input('srvcount')

    with col2:
        serrorrate = st.text_input('serrorrate')

    # code for Prediction
    # creating a button for Prediction

    if st.button('Ddos Result'):
        ddos_prediction = ddos_model.predict([[id, duration, protocoltype_encoded, service_encoded, flag_encoded, srcbytes,
                                                 dstbytes, land, wrongfragment, urgent, hot, numfailedlogins,
                                                 loggedin, numcompromised, rootshell,
                                                 suattempted, numroot, numfilecreations, numshells, numaccessfiles,
                                                 numoutboundcmds, ishostlogin,
                                                 isguestlogin, count, srvcount, serrorrate]])
        if ddos_prediction == 0:
            st.success('The output is {}. Not a DDOS ATTACK'.format(ddos_prediction))

        else:
            st.warning('The output is {}. It is a DDOS ATTACK'.format(ddos_prediction))


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

