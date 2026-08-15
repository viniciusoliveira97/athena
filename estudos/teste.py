import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]
df["empate"] = df["mandante_Placar"] == df["visitante_Placar"]
df["vitoria_visitante"] = df["mandante_Placar"] < df["visitante_Placar"]

vitorias_por_time = df.groupby("mandante")["vitoria_mandante"].sum()
empates_por_time = df.groupby("mandante")["empate"].sum()
derrotas_por_time = df.groupby("mandante")["vitoria_visitante"].sum()

time = input("Escolha o time para analisar: ")

if time in vitorias_por_time.index:
    print(f"--- {time} em casa ---")
    print("Vitórias:", vitorias_por_time.loc[time])
    print("Empates:", empates_por_time.loc[time])
    print("Derrotas:", derrotas_por_time.loc[time])
else:
    print("Time não encontrado. Verifique o nome digitado.")