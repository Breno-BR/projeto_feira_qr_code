import pandas as pd
from pandas import read_excel, read_csv, DataFrame
import sqlite3
from datetime import datetime as dt
# import qrcode

def carregar_arquivo(file):

    if 'csv' in file:
        arquivo = read_csv(file,
                           sep=';')
        return arquivo
    else:
        arquivo = read_excel(file, header=None)
        return arquivo


def sql_save_data(codigo_obj, data_atual=dt.now().strftime("%d/%m/%Y")):
    try:
        con = sqlite3.connect('dados.db')
        cur = con.cursor()
        print("Conexão realizada com sucesso!")
        qry = "INSERT INTO loec(codigo, data) VALUES(?, ?)"
        cur.execute(qry, (codigo_obj, data_atual))
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def sql_load_data(db):
    try:
        con = sqlite3.connect(db)
        cur = con.cursor()
        print("Conexão realizada com sucesso!")
        qry = "SELECT * FROM loec"
        cur.execute(qry)
        rows = cur.fetchall()
        df = DataFrame(rows)
        df.columns = ['Objeto', 'Data']
        con.close()
        return df
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)




#
# df = carregar_arquivo('Códigos.xlsx')
#
# sql_load_data('dados.db')
#
#
# len(df.iloc[0, 0])
#
#
# len(dt.now().strftime("%d/%m/%Y"))
#
# arq = df.iloc[0, 0]
# data = dt.now().strftime("%d/%m/%Y")
#
# sql_save_data(arq)

