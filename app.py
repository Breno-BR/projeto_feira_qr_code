import streamlit as st
from functions import *

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.write("")

with col2:
    st.image("Correios_DEPED.png")

with col3:
    st.write("")


# Título
'''\n'''
'''\n'''
st.title("DEPED - Locker")
'''\n'''

st.sidebar.subheader("Enviar arquivo LOEC")
arquivo = st.sidebar.file_uploader("Enviar o arquivo com os códigos dos objetos:")
if arquivo is not None:
    arquivo_carregado = carregar_arquivo(arquivo)
    arquivo_carregado.iloc[:, 0].apply(sql_save_data)
    st.table(arquivo_carregado.head())
    submitted = st.sidebar.button("Gravar LOEC")
    if submitted:
        st.sidebar.write("LOEC gravada!")