"""This modules contains data about prediction of Parkinson's disease on unseen data"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction on Unseen Data")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Parkinson's disease on unseen data.
            </p>
        """, unsafe_allow_html=True)
    with st.expander("View attribute details"):
        st.markdown("""MDVP:Fo(Hz) - Average vocal fundamental frequency\n
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency\n
MDVP:Flo(Hz) - Minimum vocal fundamental frequency\n
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several
measures of variation in fundamental frequency\n
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude\n
NHR,HNR - Two measures of ratio of noise to tonal components in the voice\n
status - Health status of the subject (one) - Parkinson's, (zero) - healthy\n
RPDE,D2 - Two nonlinear dynamical complexity measures\n
DFA - Signal fractal scaling exponent\n
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation""")
    # Take feature input from the user
    # Add a subheader
    st.subheader("Enter Values:")

    # Take input of features from the user.
    
    avff = st.number_input("Average vocal fundamental frequency", float(df["AVFF"].min()), float(df["AVFF"].max()),step=1e-3, format="%.3f")
    st.write("Range=",float(df["AVFF"].min()),"-",float(df["AVFF"].max()))

    mavff = st.number_input("Maximum vocal fundamental frequency", float(df["MAVFF"].min()), float(df["MAVFF"].max()),step=1e-3, format="%.3f")
    st.write("Range=",float(df["MAVFF"].min()),"-",float(df["MAVFF"].max()))

    mivff = st.number_input("Minimum vocal fundamental frequency", float(df["MIVFF"].min()), float(df["MIVFF"].max()),step=1e-3, format="%.3f")
    st.write("Range=",float(df["MIVFF"].min()),"-",float(df["MIVFF"].max()))

    jitddp = st.number_input("Jitter:DDP", float(df["Jitter:DDP"].min()), float(df["Jitter:DDP"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["Jitter:DDP"].min()),"-",float(df["Jitter:DDP"].max()))

    mdvpjit = st.number_input("Multidimensional Voice Program:Jitter(%)", float(df["MDVP:Jitter(%)"].min()), float(df["MDVP:Jitter(%)"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["MDVP:Jitter(%)"].min()),"-",float(df["MDVP:Jitter(%)"].max()))

    mdvprap = st.number_input("MDVP RAP", float(df["MDVP:RAP"].min()), float(df["MDVP:RAP"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["MDVP:RAP"].min()),"-",float(df["MDVP:RAP"].max()))

    mdvpapq = st.number_input("MDVP APQ", float(df["MDVP:APQ"].min()), float(df["MDVP:APQ"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["MDVP:APQ"].min()),"-",float(df["MDVP:APQ"].max()))

    mdvpppq = st.number_input("MDVP PPQ", float(df["MDVP:PPQ"].min()), float(df["MDVP:PPQ"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["MDVP:PPQ"].min()),"-",float(df["MDVP:PPQ"].max()))

    mdvpshim = st.number_input("MDVP Shimmer", float(df["MDVP:Shimmer"].min()), float(df["MDVP:Shimmer"].max()),step=1e-3, format="%.3f")
    st.write("Range=",float(df["MDVP:Shimmer"].min()),"-",float(df["MDVP:Shimmer"].max()))

    shimdda = st.number_input("Shimmer DDA", float(df["Shimmer:DDA"].min()), float(df["Shimmer:DDA"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["Shimmer:DDA"].min()),"-",float(df["Shimmer:DDA"].max()))

    shimapq3 = st.number_input("Shimmer APQ3", float(df["Shimmer:APQ3"].min()), float(df["Shimmer:APQ3"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["Shimmer:APQ3"].min()),"-",float(df["Shimmer:APQ3"].max()))

    shimapq5 = st.number_input("Shimmer APQ5", float(df["Shimmer:APQ5"].min()), float(df["Shimmer:APQ5"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["Shimmer:APQ5"].min()),"-",float(df["Shimmer:APQ5"].max()))

    nhr = st.number_input("NHR", float(df["NHR"].min()), float(df["NHR"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["NHR"].min()),"-",float(df["NHR"].max()))

    hnr = st.number_input("HNR", float(df["HNR"].min()), float(df["HNR"].max()),step=1e-3, format="%.3f")
    st.write("Range=",float(df["HNR"].min()),"-",float(df["HNR"].max()))

    rpde = st.number_input("RPDE", float(df["RPDE"].min()), float(df["RPDE"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["RPDE"].min()),"-",float(df["RPDE"].max()))

    dfa = st.number_input("DFA", float(df["DFA"].min()), float(df["DFA"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["DFA"].min()),"-",float(df["DFA"].max()))

    d2 = st.number_input("D2", float(df["D2"].min()), float(df["D2"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["D2"].min()),"-",float(df["D2"].max()))

    ppe = st.number_input("PPE", float(df["PPE"].min()), float(df["PPE"].max()),step=1e-5, format="%.5f")
    st.write("Range=",float(df["PPE"].min()),"-",float(df["PPE"].max()))

    # Create a list to store all the features
    features = [avff, mavff, mivff, jitddp, mdvpjit, mdvprap,mdvpapq,mdvpppq,mdvpshim,shimdda,shimapq3,shimapq5,nhr,hnr,rpde,dfa,d2,ppe]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.success("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person either has Parkison's disease or prone to get Parkinson's disease")
        else:
            st.info("The person is safe from Parkinson's disease")

        
