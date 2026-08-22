import pandas as pd
import sys

sys.path.append("src")

from partidas import df

df["total_gols"] = df["mandante_Placar"] + df["visitante_Placar"]

jogos_over_25 = df["total_gols"] > 2.5

def calcular_probabilidade_over(df, linha=2.5):
    total_gols = df["mandante_Placar"] + df["visitante_Placar"]
    return (total_gols > linha).mean()

probabilidade_geral = calcular_probabilidade_over(df)

partidas_palmeiras_casa = df.loc[df["mandante"] == "Palmeiras"]
probabilidade_palmeiras_casa = calcular_probabilidade_over(partidas_palmeiras_casa)

print(f"Geral: {probabilidade_geral:.1%}")
print(f"Palmeiras em casa: {probabilidade_palmeiras_casa:.1%}")