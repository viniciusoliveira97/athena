def filtrar_partidas_mandante(partidas, time):
    partidas_do_time = []

    for partida in partidas:
        if partida["mandante"] == time:
            partidas_do_time.append(partida)

    return partidas_do_time

def filtrar_partidas_visitante(partidas, time):
    partidas_do_time = []

    for partida in partidas:
        if partida["visitante"] == time:
            partidas_do_time.append(partida)

    return partidas_do_time