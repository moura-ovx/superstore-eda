import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    file_path = "data/raw/train.csv" 
    
    # encoding='latin1' lida com caracteres especiais comuns em CSVs do Kaggle
    df = pd.read_csv(file_path, encoding="latin1") 
    
    # Conversão de datas
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")

    return df