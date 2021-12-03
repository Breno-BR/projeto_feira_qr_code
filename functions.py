import os
from pandas import read_excel, read_csv, DataFrame
import sqlite3
from datetime import datetime as dt
import qrcode
from PIL import Image


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


def sql_load_data():
    try:
        con = sqlite3.connect('dados.db')
        cur = con.cursor()
        print("Conexão realizada com sucesso!")
        qry = "SELECT * FROM loec"
        cur.execute(qry)
        rows = cur.fetchall()
        df = DataFrame(rows)
        df.columns = ['Objeto', 'Data']
        df.drop_duplicates(subset='Objeto', keep='first', inplace=True)
        con.close()
        return df
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def gerar_codigo(codigo):
    qr = qrcode.QRCode()
    qr.add_data(codigo)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qr_res = img.resize((512, 512), Image.NORMAL)
    qr_res.save(str(codigo)+'.png')


def sql_del_data(codigo):
    try:
        con = sqlite3.connect('dados.db')
        cur = con.cursor()
        print("Conexão realizada com sucesso!")
        qry = "DELETE FROM loec WHERE codigo=?"
        cur.execute(qry, (codigo,))
        print(cur.fetchall())
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def remove_img(codigo):
    imgs = [i for i in os.listdir(".") if i.endswith(".png")]
    check = any([i.startswith(codigo) for i in imgs])
    if check:
        os.remove(f'{codigo}.png')


def has_data():
    con = sqlite3.connect('dados.db')
    cur = con.cursor()
    print("Conexão realizada com sucesso!")
    qry = "SELECT * FROM loec"
    cur.execute(qry)
    rows = cur.fetchall()
    df = DataFrame(rows)
    if len(df) != 0:
        return True
    con.close()


def apagar_base():
    con = sqlite3.connect('dados.db')
    cur = con.cursor()
    print("Conexão realizada com sucesso!")
    qry = "DELETE FROM loec"
    cur.execute(qry)
    print(cur.fetchall())
    con.commit()
    con.close()


