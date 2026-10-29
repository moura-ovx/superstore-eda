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

# Aplica a combinação lógica entre duas Series do Pandas
df_filtered = df[(df["Region"].isin(regioes)) & (df["Category"].isin(categorias))]

# Métricas Principais (KPIs)
total_vendas = df_filtered["Sales"].sum()
total_pedidos = df_filtered["Order ID"].nunique()
ticket_medio = total_vendas / total_pedidos if total_pedidos > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total", f"$ {total_vendas:,.2f}")
col2.metric("Total de Pedidos", f"{total_pedidos:,}")
col3.metric("Ticket Médio", f"$ {ticket_medio:,.2f}")

st.divider()

# Visualizações
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Vendas por Subcategoria")
    vendas_subcat = df_filtered.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=True)
    st.bar_chart(vendas_subcat)

with col_right:
    st.subheader("Evolução das Vendas no Tempo")
    vendas_tempo = df_filtered.set_index("Order Date").resample("ME")["Sales"].sum()
    st.line_chart(vendas_tempo)

# Tabela de Dados
with st.expander("Visualizar tabela de dados completa"):
    st.dataframe(df)