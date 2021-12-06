import streamlit as st
from functions import *
import os

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

# imagem = 'blank.jpg'
lidos = 0

if 'executar' not in st.session_state:
    st.session_state['executar'] = 0

if has_data():
    df = sql_load_data()
    with st.form("my_form"):
        if has_data():
            st.subheader("Objetos cadastrados")
            '''\n'''
            # df = sql_load_data()
            df.iloc[:, 0].apply(gerar_codigo)
            for i in range(0, len(df)):
                df = sql_load_data()
                col1, col2, col3 = st.columns(3) #, col4 = st.columns(4)
                with st.container():
                    with col1:
                        st.write(f'{i+1} - {df.iloc[i, 0]}')
                    with col2:
                        imgs = [i.split('.')[0] for i in os.listdir(".") if i.endswith(".png")]
                        if (df.iloc[i, 0] in imgs):
                            st.image(f'{df.iloc[i, 0]}.png')
                    with col3:
                        if st.checkbox(label='Leitura realizada', key=df.iloc[i, 0]):
                            lidos += 1
                            print(lidos)
                            # print(df.iloc[:, 0].nunique())
                    # with col4:
                    #     if st.button("Delete", key=f'{df.iloc[i, 0]}'):
                    #         sql_del_data(df.iloc[i, 0])
                    #         remove_img(df.iloc[i, 0])
                    #         st.warning(f'{df.iloc[i, 0]} removido!')
            submitted = st.form_submit_button("Verificar leitura")
            if submitted:
                if lidos == len(df):
                    st.session_state.executar = 1
                    st.balloons()
                else:
                    st.session_state.executar = 0
                    st.warning('Existem objetos pendentes de leitura!')
    '''\n'''
    st.button("Apagar base de dados", key='apagar', on_click=apagar_base(df))


else:
    st.warning("Base de dados sem objetos cadastrados. Envie o arquivo da LOEC.")
    st.subheader("Enviar arquivo LOEC")
    arquivo = st.file_uploader("Enviar o arquivo com os códigos dos objetos:")
    if arquivo is not None:
        arquivo_carregado = carregar_arquivo(arquivo)
        arquivo_carregado.iloc[:, 0].apply(sql_save_data)
        st.experimental_rerun()

        # submitted = st.button("Gravar LOEC")
        # if submitted:
        #     arquivo_carregado.iloc[:, 0].apply(sql_save_data)
        #     st.warning("LOEC gravada!")
        #     st.session_state.update()

#
# else:
#     st.warning("Base de dados sem objetos cadastrados. Envie o arquivo da LOEC.")

#
#
# if imagem != 'blank.jpg':
#     st.sidebar.header(imagem.strip(".png"))
#     st.sidebar.image(imagem)

# st.sidebar.subheader("Enviar arquivo LOEC")
# arquivo = st.sidebar.file_uploader("Enviar o arquivo com os códigos dos objetos:")
# if arquivo is not None:
#     arquivo_carregado = carregar_arquivo(arquivo)
#     submitted = st.sidebar.button("Gravar LOEC")
#     if submitted:
#         arquivo_carregado.iloc[:, 0].apply(sql_save_data)
#         st.sidebar.warning("LOEC gravada. Atualize a página.")