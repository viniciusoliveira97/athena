import sqlite3
import pandas as pd

CAMINHO_BANCO = "data/athena.db"


def criar_banco(df):
    conexao = sqlite3.connect(CAMINHO_BANCO)
    df.to_sql("partidas", conexao, if_exists="replace", index=False)
    conexao.close()


def buscar_partidas_time(time):
    conexao = sqlite3.connect(CAMINHO_BANCO)

    consulta = "SELECT * FROM partidas WHERE mandante = ?"
    resultado = pd.read_sql_query(consulta, conexao, params=(time,))

    conexao.close()
    return resultado