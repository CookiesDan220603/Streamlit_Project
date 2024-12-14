import streamlit as st
import pandas as pd
import numpy as np
import pickle4 as pickle 
@st.cache_resource
def get_fvalue(val):    
    feature_dict = {"No": 1, "Yes": 2}    
    return feature_dict[val]
def get_value(val, my_dict):    
    return my_dict[val]


app_mode = st.sidebar.selectbox("Home page selection", ["Home", "Prediction"])

if app_mode == 'Home':    
    st.title('Loan Prediction')    
    st.image('loan_image.jpg')    
    st.markdown('Dataset:')    
    data = pd.read_csv('shopping_data.csv')    
    st.write(data.head())    
    st.bar_chart(data[['Purchase Amount (USD)', 'Age']].head(20))
    