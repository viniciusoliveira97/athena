partida = {
    "time_mandante": "Corinthians",
    "time_visitante": "Remo",
    "gols_mandante": 0,
    "gols_visitante": 4
}
total_gols = partida["gols_mandante"] + partida["gols_visitante"]
saldo_gols = partida["gols_mandante"] - partida["gols_visitante"]
if partida["gols_mandante"] > partida["gols_visitante"]:
    resultado = "Vitória do mandante"
elif partida["gols_mandante"] == partida["gols_visitante"]:
    resultado = "Empate"
else:
    resultado = "Vitória visitante"
print("Time mandante:", partida["time_mandante"])
print("Time visiante:", partida["time_visitante"])
print("Gols mandante:", partida["gols_mandante"])
print("Gols visitante:", partida["gols_visitante"])
print("Total de gols:", total_gols)
print("Saldo de gols:", saldo_gols)
print("Resultado:", resultado)

-------------------------------

gols = [3, 1, 2, 0, 4, 5, 2]
print("Primeiro jogo:", gols[5])

--------------------------------

partidas = [
    {
        "time_mandante": "Corinthians",
        "time_visitante": "Remo",
        "gols_mandante": 2,
        "gols_visitante": 1
    },
    {
        "time_mandante": "Palmeiras",
        "time_visitante": "Santos",
        "gols_mandante": 3,
        "gols_visitante": 0
    },
    {
        "time_mandante": "Flamengo",
        "time_visitante": "Botafogo",
        "gols_mandante": 1,
        "gols_visitante": 1
    }
]

vitorias_mandante = 0
vitorias_visitante = 0
empates = 0

for partida in partidas:
    print(
        partida["time_mandante"],
        partida["gols_mandante"],
        "x",
        partida["gols_visitante"],
        partida["time_visitante"]
    )

    if partida["gols_mandante"] > partida["gols_visitante"]:
        print("Resultado: Vitória do mandante")
        vitorias_mandante = vitorias_mandante + 1
        print()

    elif partida["gols_mandante"] == partida["gols_visitante"]:
        print("Resultado: Empate")
        empates = empates +1
        print()

    else:
        print("Resultado: Vitória do visitante")
        vitorias_visitante = vitorias_visitante + 1
        print()

print("----------------------------")
print("RESUMO:")
print("Vitórias do mandante:", vitorias_mandante)
print("Empates:", empates)
print("Vitórias do visitante:", vitorias_visitante)