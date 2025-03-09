# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:27:02 2024

@author: Dell
"""

# importing libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('D:/AIML Projects/Multiple Disease Prediction System/Saved models/trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('D:/AIML Projects/Multiple Disease Prediction System/Saved models/trained_model_heart.sav', 'rb'))
parkinsons_model = pickle.load(open('D:/AIML Projects/Multiple Disease Prediction System/Saved models/trained_model_parkinsons.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    select = option_menu("Multiple Disease Prediction System",
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         icons=['activity','heart-pulse-fill', 'person'],
                         default_index = 0)
    
# diabetes prediction page
if(select=='Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for predict
    if st.button('Diabetes Test Result'):
        pred = diabetes_model.predict([Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                         Insulin, BMI, DiabetesPedigreeFunction, Age])
        if(pred[0] == 0):
            diagnosis = 'The person is not diabetic.'
        else:
            diagnosis = 'The person is diabetic.'
        
    st.success(diagnosis)
    
    
    
    
if(select=='Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cpt = st.text_input('Chest Pain Types')
    with col1:
        rbp = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (values 0,1,2)')
    with col2:
        mhr = st.text_input('Maximum heart rate acheived')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise')
    with col3:
        ca = st.text_input('Number of major vessels coloured by fluorosopy')
    with col1:
        thal = st.text_input('thal: 0=normal; 1=fixed defect; 2=reversable defect')
    
    
    heart_diagnosis = ''
    if(st.button('Heart Disease Prediction')):
        heart_prediction = heart_disease_model.predict([age, sex, cpt, rbp, chol, fbs, restecg, mhr, exang, oldpeak, slope, ca, thal])
        
        if(heart_prediction[0] == 1):
            heart_diagnosis = "The person is having heart disease."
        else:
            heart_diagnosis = "The person is not having a heart disease."
            
    st.success(heart_diagnosis)
    
    
    
    
    
if(select=='Parkinsons Prediction'):
    # page title
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        name = st.text_input('Name')
    with col2:
        mdvpfo = st.text_input('MDVP:Fo(Hz)')
    with col3:
        mdvpfhi = st.text_input('MDVP:Fhi(Hz)')
    with col4:
        mdvpflo = st.text_input('MDVP:Flo(Hz)')
    with col5:
        mdvpjitterPer = st.text_input('MDVP:Jitter(%)')
    with col1:
        mdvpjitterAbs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        mdvpRap = st.text_input('MDVP:RAP')
    with col3:
        mdvpPpq = st.text_input('MDVP:PPQ')
    with col4:
        mdvpDdp = st.text_input('Jitter:DDP')
    with col5:
        mdvpSh = st.text_input('MDVP:Shimmer')
    with col1:
        mdvpShDb = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        shimmer1 = st.text_input('Shimmer:APQ3')
    with col3:
        shimmer2 = st.text_input('Shimmer:APQ5')
    with col4:
         mdvpApq = st.text_input('MDVP:APQ')
    with col5:
         shimmer3 = st.text_input('Shimmer:DDA')
    with col1:
         nhr = st.text_input('NHR')
    with col2:
        shimmer2 = st.text_input('HNR') 
    with col3:
         rpde = st.text_input('RPDE')
    with col4:
         d2 = st.text_input('D2')
    with col5:
        dfa = st.text_input('DFA')
    with col1:
         s1 = st.text_input('Spread1')
    with col2:
         s2 = st.text_input('Spread2')
    with col3:
         ppe = st.text_input('PPE')
    
    
    
