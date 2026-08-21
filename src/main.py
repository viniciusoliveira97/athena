from partidas import df
from estatisticas import calcular_resumo_mandante, calcular_resumo_visitante, calcular_dispersao_gols, calcular_dispersao_gols_time
 
resumo_mandante = calcular_resumo_mandante(df)
resumo_visitante = calcular_resumo_visitante(df)
 
dispersao_mandante = calcular_dispersao_gols(df, "mandante_Placar")
dispersao_visitante = calcular_dispersao_gols(df, "visitante_Placar")
 
print("--- Dispersão de gols do mandante ---")
print(dispersao_mandante)
 
print("--- Dispersão de gols do visitante ---")
print(dispersao_visitante)
 
while True:
    time = input("Escolha o time para analisar (ou 'sair' para encerrar): ")
 
    if time == "sair":
        break
 
    if time not in resumo_mandante.index:
        print("Time não encontrado. Verifique o nome digitado.")

    else:
        print(f"\n--- {time} em casa ---")
        print(resumo_mandante.loc[[time]])

        dispersao_time = calcular_dispersao_gols_time(df, time)
        print(f"Dispersão de gols em casa: {dispersao_time}")

        print(f"\n--- {time} fora ---")
        print(resumo_visitante.loc[[time]])
 
    print()
 
print("Programa encerrado.")