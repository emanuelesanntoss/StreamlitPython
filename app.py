import streamlit as st
import pandas as pd

st.set_page_config(page_title="Site Streamlit")

#Conteiner_1
with st.container():
    #st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://streamlit.io/)")

@st.cache_data
#retornar os dados
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

#Conteiner_2
with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")

