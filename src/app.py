import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Dashboard de Vendas - Kaggle", layout="wide")

st.title("Análise de Vendas: Superstore (Kaggle)")
st.markdown("Dashboard interativo utilizando dados reais do Kaggle.")

df = load_data()

# Barra Lateral
st.sidebar.header("Filtros Comerciais")
    
regioes = st.sidebar.multiselect(
    "Selecione a Região:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)
    
categorias = st.sidebar.multiselect(
    "Selecione a Categoria:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)