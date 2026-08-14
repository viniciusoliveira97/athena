def calcular_estatisticas(partidas):
    vitorias_mandante = 0
    empates = 0
    vitorias_visitante = 0
    partidas_com_erro = 0

    for partida in partidas:
        try:
            gols_mandante = int(partida["mandante_Placar"])
            gols_visitante = int(partida["visitante_Placar"])
        except ValueError:
            partidas_com_erro = partidas_com_erro + 1
            continue

        if gols_mandante > gols_visitante:
            vitorias_mandante = vitorias_mandante + 1
        elif gols_mandante == gols_visitante:
            empates = empates + 1
        else:
            vitorias_visitante = vitorias_visitante + 1

    return {
        "vitorias_mandante": vitorias_mandante,
        "empates": empates,
        "vitorias_visitante": vitorias_visitante,
        "partidas_com_erro": partidas_com_erro,
    }