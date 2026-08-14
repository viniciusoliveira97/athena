import csv

def contar_vitorias_mandante(partidas):
    vitorias_mandante = 0

    for partida in partidas:
        gols_mandante = int(partida["mandante_Placar"])
        gols_visitante = int(partida["visitante_Placar"])

        if gols_mandante > gols_visitante:
            vitorias_mandante = vitorias_mandante + 1

    return vitorias_mandante


with open("data/campeonato-brasileiro-full.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    partidas = list(leitor)

resultado = contar_vitorias_mandante(partidas)
print("Vitórias do mandante:", resultado)