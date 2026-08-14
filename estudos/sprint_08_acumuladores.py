partidas = [
    {
        "time_mandante": "Juventude",
        "time_visitante": "Avai",
        "gols_mandante": 1,
        "gols_visitante": 0
    },
    {
        "time_mandante": "Ponte Preta",
        "time_visitante": "Athletic Club",
        "gols_mandante": 1,
        "gols_visitante": 1
    },
    {
        "time_mandante": "Fortaleza",
        "time_visitante": "Botafogo-SP",
        "gols_mandante": 1,
        "gols_visitante": 0
    }
]

total_gols_mandante = 0
total_gols_visitante = 0

for partida in partidas:
    total_gols_mandante = total_gols_mandante + partida["gols_mandante"]
    total_gols_visitante = total_gols_visitante + partida["gols_visitante"]

print("Gols Mandante:", total_gols_mandante)
print("Gols Visitante:" ,total_gols_visitante)













print(total_gols_mandante)