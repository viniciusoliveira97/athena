from partidas import df

resumo_mandante = df.groupby("mandante").agg(
    jogos=("mandante", "size"),
    vitorias=("vitoria_mandante", "sum"),
    empates=("empate", "sum"),
    derrotas=("vitoria_visitante", "sum")
)

resumo_visitante = df.groupby("visitante").agg(
    jogos=("visitante", "size"),
    vitorias=("vitoria_visitante", "sum"),
    empates=("empate", "sum"),
    derrotas=("vitoria_mandante", "sum")
)

while True:
    time = input("Escolha o time para analisar (ou 'sair' para encerrar): ")

    if time == "sair":
        break

    if time not in resumo_mandante.index:
        print("Time não encontrado. Verifique o nome digitado.")
    else:
        print(f"\n--- {time} em casa ---")
        print(resumo_mandante.loc[[time]])

        print(f"\n--- {time} fora ---")
        print(resumo_visitante.loc[[time]])

    print()

print("Programa encerrado.")