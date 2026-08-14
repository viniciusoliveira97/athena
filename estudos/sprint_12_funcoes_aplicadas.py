receber_gols()
descobrir_resultado()
somar_gols()
mostrar_resumo()

gols_mandante = receber_gols("mandante")
gols_visitante = receber_gols("visitante")

resultado = descobrir_resultado(gols_mandante, gols_visitante)

total_gols = somar_gols(gols_mandante, gols_visitante)

mostrar_resumo(gols_mandante, gols_visitante, resultado, total_gols)
--------------------------------------------------------------

def descobrir_resultado(gols_mandante, gols_visitante):

    if gols_mandante > gols_visitante:
        return "Vitória do mandante"

    elif gols_mandante == gols_visitante:
        return "Empate"

    else:
        return "Vitória do visitante"
-----------------------------------------------------------

def somar_gols(gols_mandante, gols_visitante):
    return gols_mandante + gols_visitante


def descobrir_resultado(gols_mandante, gols_visitante):

    if gols_mandante > gols_visitante:
        return "Vitória do mandante"

    elif gols_mandante == gols_visitante:
        return "Empate"

    else:
        return "Vitória do visitante"


def mostrar_resumo(gols_mandante, gols_visitante, total, resultado):
    print("Gols do mandante:", gols_mandante)
    print("Gols do visitante:", gols_visitante)
    print("Total de gols:", total)
    print("Resultado:", resultado)


gols_mandante = 2
gols_visitante = 2

total = somar_gols(gols_mandante, gols_visitante)

resultado = descobrir_resultado(gols_mandante, gols_visitante)

mostrar_resumo(gols_mandante, gols_visitante, total, resultado)
-----------------------------------------------------------

def calcular_media_gols(total_gols, quantidade_partidas):
    media = total_gols / quantidade_partidas
    return media


media_campeonato = calcular_media_gols(12, 4)

print("Média de gols:", media_campeonato)

--------------------------------------------------------------

def contar_empates(partidas):
    empates = 0

    for partida in partidas:
        if partida["gols_mandante"] == partida["gols_visitante"]:
            empates = empates + 1

    return empates


partidas = [
    {"gols_mandante": 2, "gols_visitante": 1},
    {"gols_mandante": 0, "gols_visitante": 0},
    {"gols_mandante": 1, "gols_visitante": 3},
    {"gols_mandante": 4, "gols_visitante": 2},
]

resultado = contar_empates(partidas)
print("Empates:", resultado)