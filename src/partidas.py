import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["ano"] = df["data"].dt.year

df["temporada"] = df["ano"]
df.loc[(df["ano"] == 2021) & (df["data"] <= "2021-02-25"), "temporada"] = 2020

df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]
df["empate"] = df["mandante_Placar"] == df["visitante_Placar"]
df["vitoria_visitante"] = df["mandante_Placar"] < df["visitante_Placar"]

from banco import criar_banco

criar_banco(df)