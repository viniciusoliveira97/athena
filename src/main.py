from partidas import partidas
from estatisticas import calcular_estatisticas
from filtros import filtrar_partidas_mandante, filtrar_partidas_visitante

while True:
    time = input("Escolha o time para analisar (ou 'sair' para encerrar): ")

    if time == "sair":
        break

    partidas_casa = filtrar_partidas_mandante(partidas, time)
    partidas_fora = filtrar_partidas_visitante(partidas, time)

    if len(partidas_casa) == 0:
        print("Time não encontrado. Verifique o nome digitado.")
    else:
        resultado_casa = calcular_estatisticas(partidas_casa)
        resultado_fora = calcular_estatisticas(partidas_fora)

        print("--- ", time, " em casa ---")
        print("Jogos:", len(partidas_casa))
        print("Vitórias:", resultado_casa["vitorias_mandante"])
        print("Empates:", resultado_casa["empates"])
        print("Derrotas:", resultado_casa["vitorias_visitante"])

        print("--- ", time, " fora ---")
        print("Jogos:", len(partidas_fora))
        print("Empates:", resultado_fora["empates"])
        print("Vitórias:", resultado_fora["vitorias_visitante"])
        print("Derrotas:", resultado_fora["vitorias_mandante"])

    print()  # linha em branco para separar visualmente cada consulta

print("Programa encerrado.")