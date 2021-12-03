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

imagem = 'blank.jpg'

if has_data():
    st.subheader("Objetos cadastrados")
    '''\n'''
    df = sql_load_data()

    for i in range(0, len(df)):
        col1, col2, col3 = st.columns(3)
        with st.container():
            with col1:
                st.write(df.iloc[i, 0])
            with col2:
                if st.button("QR Code", key=f'{df.iloc[i, 0]}'):
                    gerar_codigo(df.iloc[i, 0])
                    imagem = f'{df.iloc[i, 0]}.png'
            # with col3:
            #     st.write(df.iloc[i, 1])
            with col3:
                if st.button("Delete", key=f'{df.iloc[i, 0]}'):
                    sql_del_data(df.iloc[i, 0])
                    remove_img(df.iloc[i, 0])
                    st.warning(f'{df.iloc[i, 0]} removido!')

    '''\n'''
    if st.button("Apagar base de dados", key='apagar'):
        st.error("Tem certeza que deseja apagar todos os dados?")
        st.button('SIM', key='sim', on_click=apagar_base())

else:
    st.warning("Base de dados sem objetos cadastrados. Envie o arquivo da LOEC.")



if imagem != 'blank.jpg':
    st.sidebar.header(imagem.strip(".png"))
    st.sidebar.image(imagem)

st.sidebar.subheader("Enviar arquivo LOEC")
arquivo = st.sidebar.file_uploader("Enviar o arquivo com os códigos dos objetos:")
if arquivo is not None:
    arquivo_carregado = carregar_arquivo(arquivo)
    submitted = st.sidebar.button("Gravar LOEC")
    if submitted:
        arquivo_carregado.iloc[:, 0].apply(sql_save_data)
        st.sidebar.warning("LOEC gravada. Atualize a página.")