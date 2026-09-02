import sys
sys.path.append("src")

from partidas import df

df_ordenado = df.sort_values("data")

ratings = {}
rating_inicial = 1500
k = 30

historico_elo = []

for _, partida in df_ordenado.iterrows():
    mandante = partida["mandante"]
    visitante = partida["visitante"]

    rating_mandante = ratings.get(mandante, rating_inicial)
    rating_visitante = ratings.get(visitante, rating_inicial)

    expectativa_mandante = 1 / (1 + 10 ** ((rating_visitante - rating_mandante) / 400))

    if partida["vitoria_mandante"]:
        resultado_mandante = 1
    elif partida["empate"]:
        resultado_mandante = 0.5
    else:
        resultado_mandante = 0

    novo_rating_mandante = rating_mandante + k * (resultado_mandante - expectativa_mandante)
    novo_rating_visitante = rating_visitante + k * ((1 - resultado_mandante) - (1 - expectativa_mandante))

    ratings[mandante] = novo_rating_mandante
    ratings[visitante] = novo_rating_visitante

    historico_elo.append({
        "data": partida["data"],
        "mandante": mandante,
        "visitante": visitante,
        "rating_mandante_pos": novo_rating_mandante,
        "rating_visitante_pos": novo_rating_visitante
    })

ranking_elo = sorted(ratings.items(), key=lambda item: item[1], reverse=True)

for time, rating in ranking_elo[:10]:
    print(time, round(rating, 1))