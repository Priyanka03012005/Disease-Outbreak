import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='👩‍⚕️')

diabetes_model= pickle.load(open(r"saved_models\diabetes_model.ssv",'rb'))

heart_model= pickle.load(open(r"saved_models\heart_model.ssv",'rb'))

parkinsons_model= pickle.load(open(r"saved_models\parkinsons_model.ssv",'rb'))

with st.sidebar:
    selected=option_menu('Prediction of disease outbreak',['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of  Pregnancies')
    with col2:
        Glucose=  st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFuction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of  the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFuction, Age]
        if "" in user_input:
            st.error("Please fill out all fields before proceeding.")
        else:
            user_input=[float(x) for x in user_input]
            diab_prediction= diabetes_model.predict([user_input])
            if diab_prediction[0]==1:
                diab_diagnosis='The person is diabetic'
            else:
                diab_diagnosis= 'The person is not diabetic'
            st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.selectbox("Gender", options=[None, 1, 0], 
                           format_func=lambda x: "Select" if x is None else ["Male", "Female"][x] )
    with col3:
        cp = st.selectbox("Chest Pain Type", options=[None, 0, 1, 2, 3], 
                          format_func=lambda x: "Select" if x is None else ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[None, 1, 0], 
                           format_func=lambda x: "Select" if x is None else ["True", "False"][x])
    with col1:
        restecg = st.selectbox("Resting ECG Results", options=[None, 0, 1, 2], 
                               format_func=lambda x: "Select" if x is None else ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"][x])
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[None, 1, 0], 
                             format_func=lambda x: "Select" if x is None else ["Yes", "No"][x])
    with col1:
        oldpeak = st.text_input('ST Depression Induced ')
    with col2:
        slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[None, 0, 1, 2], 
                             format_func=lambda x: "Select" if x is None else ["Upsloping", "Flat", "Downsloping"][x])
    with col3:
        ca = st.selectbox("Number of Major Vessels", options=[None, 0, 1, 2, 3, 4], 
                          format_func=lambda x: "Select" if x is None else str(x))
    with col1:
        thal = st.selectbox("Thalassemia Type", options=[None, 0, 1, 2, 3], 
                            format_func=lambda x: "Select" if x is None else ["Unknown", "Normal", "Fixed Defect", "Reversible Defect"][x])
    heart_diagnosis = ""
    if st.button('Heart Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        if None in user_input or "" in user_input:
            st.error("Please fill out all fields before proceeding.")
        else:
            user_input = [float(x) for x in user_input]  
            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease 😞'
            else:
                heart_diagnosis = 'The person does not have heart disease 😊'

            st.success(heart_diagnosis)

elif selected == 'Parkinsons prediction':
    st.title("Parkinsons Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP: Fo (Hz) - Average vocal fundamental frequency')
    
    with col2:
        fhi = st.text_input('MDVP: Fhi (Hz) - Maximum vocal fundamental frequency')
    
    with col3:
        flo = st.text_input('MDVP: Flo (Hz) - Minimum vocal fundamental frequency')
    
    with col1:
        jitter_percent = st.text_input('Jitter (%) - Frequency variation')
    
    with col2:
        jitter_abs = st.text_input('Jitter (Abs) - Absolute frequency variation')
    
    with col3:
        rap = st.text_input('RAP - Relative amplitude perturbation')
    
    with col1:
        ppq = st.text_input('PPQ - Pitch perturbation quotient')
    
    with col2:
        ddp = st.text_input('DDP - Degree of perturbation')
    
    with col3:
        shimmer = st.text_input('Shimmer - Amplitude variation')
    
    with col1:
        shimmer_db = st.text_input('Shimmer (dB) - Amplitude variation in dB')
    
    with col2:
        nhr = st.text_input('NHR - Noise-to-harmonics ratio')
    
    with col3:
        hnr = st.text_input('HNR - Harmonics-to-noise ratio')
    
    with col1:
        rpde = st.text_input('RPDE - Recurrence period density entropy')
    
    with col2:
        dfa = st.text_input('DFA - Detrended fluctuation analysis')
    
    with col3:
        spread1 = st.text_input('Spread1 - Nonlinear measure of fundamental frequency variation')
    
    with col1:
        spread2 = st.text_input('Spread2 - Nonlinear measure of fundamental frequency variation')
    
    with col2:
        d2 = st.text_input('D2 - Correlation dimension')
    
    with col3:
        ppe = st.text_input('PPE - Pitch period entropy')
    
    parkinsons_diagnosis = ""
    
    if st.button("Parkinsons Test Result"):
        user_input = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        
        if "" in user_input:
            st.error("Please fill out all fields before proceeding.")
        else:
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease 😞"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease 😊"
            
            st.success(parkinsons_diagnosis)

