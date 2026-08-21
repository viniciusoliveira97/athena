def calcular_resumo_mandante(df):
    resumo = df.groupby("mandante").agg(
        jogos=("mandante", "size"),
        vitorias=("vitoria_mandante", "sum"),
        empates=("empate", "sum"),
        derrotas=("vitoria_visitante", "sum")
    )
    return resumo


def calcular_resumo_visitante(df):
    resumo = df.groupby("visitante").agg(
        jogos=("visitante", "size"),
        empates=("empate", "sum"),
        vitorias=("vitoria_visitante", "sum"),
        derrotas=("vitoria_mandante", "sum")
    )
    return resumo


def calcular_dispersao_gols(df, coluna):
    media = df[coluna].mean()
    mediana = df[coluna].median()
    desvio = df[coluna].std()

    return {
        "media": round(media, 2),
        "mediana": mediana,
        "desvio_padrao": round(desvio, 2)
    }

def calcular_dispersao_gols_time(df, time):
    partidas_time = df.loc[df["mandante"] == time]
    return calcular_dispersao_gols(partidas_time, "mandante_Placar")