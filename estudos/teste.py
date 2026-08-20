import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["ano"] = df["data"].dt.year

df["temporada"] = df["ano"]

df.loc[(df["ano"] == 2021) & (df["data"] <= "2021-02-25"), "temporada"] = 2020

jogos_chape_2016 = df.loc[
    (df["temporada"] == 2016) & ((df["mandante"] == "Chapecoense") | (df["visitante"] == "Chapecoense"))
]

print("Total de jogos da Chape em 2016:", len(jogos_chape_2016))