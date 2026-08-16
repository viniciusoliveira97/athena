import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]
df["empate"] = df["mandante_Placar"] == df["visitante_Placar"]
df["vitoria_visitante"] = df["mandante_Placar"] < df["visitante_Placar"]

time_a = input("Escolha o primeiro time: ")
time_b = input("Escolha o segundo time: ")

confronto_geral = df.loc[
    ((df["mandante"] == time_a) & (df["visitante"] == time_b)) |
    ((df["mandante"] == time_b) & (df["visitante"] == time_a))
]

if len(confronto_geral) == 0:
    print("Nenhum confronto encontrado com esses times.")
else:
    vitorias_a = (
        ((confronto_geral["mandante"] == time_a) & confronto_geral["vitoria_mandante"]) |
        ((confronto_geral["visitante"] == time_a) & confronto_geral["vitoria_visitante"])
    ).sum()

    vitorias_b = (
        ((confronto_geral["mandante"] == time_b) & confronto_geral["vitoria_mandante"]) |
        ((confronto_geral["visitante"] == time_b) & confronto_geral["vitoria_visitante"])
    ).sum()

    empates_confronto = confronto_geral["empate"].sum()

    print(f"--- Confronto geral: {time_a} x {time_b} desde 2003 ---")
    print("Jogos:", len(confronto_geral))
    print(f"Vitórias {time_a}:", vitorias_a)
    print("Empates:", empates_confronto)
    print(f"Vitórias {time_b}:", vitorias_b)

    confronto_a_casa = df.loc[(df["mandante"] == time_a) & (df["visitante"] == time_b)]
    confronto_b_casa = df.loc[(df["mandante"] == time_b) & (df["visitante"] == time_a)]

    print(f"\n--- {time_a} em casa ---")
    print("Jogos:", len(confronto_a_casa))
    print(f"Vitórias {time_a}:", confronto_a_casa["vitoria_mandante"].sum())
    print("Empates:", confronto_a_casa["empate"].sum())
    print(f"Vitórias {time_b}:", confronto_a_casa["vitoria_visitante"].sum())

    print(f"\n--- {time_b} em casa ---")
    print("Jogos:", len(confronto_b_casa))
    print(f"Vitórias {time_b}:", confronto_b_casa["vitoria_mandante"].sum())
    print("Empates:", confronto_b_casa["empate"].sum())
    print(f"Vitórias {time_a}:", confronto_b_casa["vitoria_visitante"].sum())