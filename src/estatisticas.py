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

def calcular_probabilidade_over(df, linha=2.5):
    total_gols = df["mandante_Placar"] + df["visitante_Placar"]
    return (total_gols > linha).mean()

def calcular_tabela_over(df):
    linhas = [0.5, 1.5, 2.5, 3.5]

    probabilidades = {}
    for linha in linhas:
        chave = f"over {linha}"
        valor = calcular_probabilidade_over(df, linha)
        probabilidades[chave] = f"{valor:.2%}"

    return probabilidades

def calcular_indices_forca(df, time, temporada_inicio=None, temporada_fim=None):
    if temporada_inicio is not None:
        df = df.loc[df["temporada"] >= temporada_inicio]

    if temporada_fim is not None:
        df = df.loc[df["temporada"] <= temporada_fim]

    media_gols_liga = df["mandante_Placar"].mean()
    media_gols_sofridos_liga = df["visitante_Placar"].mean()

    partidas_time = df.loc[df["mandante"] == time]

    indice_ofensivo = partidas_time["mandante_Placar"].mean() / media_gols_liga
    indice_defensivo = partidas_time["visitante_Placar"].mean() / media_gols_sofridos_liga

    return {
        "indice_ofensivo": round(indice_ofensivo, 2),
        "indice_defensivo": round(indice_defensivo, 2)
    }