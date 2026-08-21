📘 Sprint 18 — Correção de Dados (Temporada 2020/2021) e Migração Completa para Pandas
🎯 Objetivo

Investigar e corrigir uma distorção real nos dados (temporadas 2020/2021 misturadas pela pandemia), e migrar definitivamente o Athena (partidas.py e main.py) de leitura manual com csv para Pandas.

🧠 Investigando a anomalia da pandemia

Partindo da observação de que 2020 e 2021 tinham números de jogos fora do padrão (268 e 492, em vez de ~380), a investigação seguiu esta ordem:

1. Confirmar o período real de cada ano rotulado:

periodo_2020 = df.loc[df["ano"] == 2020]
periodo_2021 = df.loc[df["ano"] == 2021]

print("2020 - primeira partida:", periodo_2020["data"].min())
print("2020 - última partida:", periodo_2020["data"].max())
print("2021 - primeira partida:", periodo_2021["data"].min())
print("2021 - última partida:", periodo_2021["data"].max())

Resultado: temporada rotulada como "2020" foi de 08/08/2020 a 27/12/2020 (268 jogos); "2021" foi de 06/01/2021 a 09/12/2021 (492 jogos) — evidência de que o calendário civil não corresponde à temporada esportiva real, por causa do atraso da pandemia.

2. Usar a coluna de rodada como evidência concreta, em vez de "achar" uma data de corte no escuro:

inicio_2021_provavel = df.loc[(df["ano"] == 2021) & (df["data"] <= "2021-03-01")]

print(inicio_2021_provavel[["data", "rodata"]].sort_values("data"))

Resultado: a rodada 38 (última rodada de um campeonato de 38 rodadas) aconteceu em 25/02/2021 — confirmando que todas as partidas rotuladas como "2021" até essa data pertencem, na verdade, à temporada esportiva 2020.

🔧 Corrigindo com uma coluna de "temporada real"
df["temporada"] = df["ano"]

df.loc[(df["ano"] == 2021) & (df["data"] <= "2021-02-25"), "temporada"] = 2020

Destrinchamento:

df["temporada"] = df["ano"] — cria a coluna temporada como cópia inicial da coluna ano (ponto de partida: assume ano civil = temporada, exceto onde será corrigido).

df.loc[condição, "coluna"] = valor — novidade importante: .loc[] pode ser usado não só para ler/filtrar dados, mas também para atribuir um valor a uma seleção específica de linhas e colunas. Sintaxe: condição antes da vírgula, nome da coluna depois, valor à direita do =.

A condição composta ((df["ano"] == 2021) & (df["data"] <= "2021-02-25")) seleciona exatamente as partidas mal rotuladas, atribuindo 2020 à coluna temporada nessas linhas.

Resultado da correção — validado com df.groupby("temporada").size():

temporada  jogos
2020         380
2021         380
(demais anos com 380, exceto anos com formatos diferentes de campeonato: 2003/2004 com mais times, e 2016 com 379)
📌 Comparação de datas em Pandas: formato ISO (AAAA-MM-DD)

Comparar df["data"] com uma string como "2021-02-25" funciona de forma confiável porque esse é o formato ISO 8601 (ano-mês-dia com hífens), interpretado pelo Pandas sem ambiguidade. Formatos como "25/02/2021" podem funcionar por coincidência em datas onde o dia não pode ser confundido com mês (ex: 25), mas são ambíguos em geral (ex: "05/02/2021" poderia ser interpretado como dia/mês ou mês/dia) — por isso o formato ISO é a prática recomendada ao comparar datas por texto em Pandas.

⚠️ O caso da Chapecoense (2016)

Ao investigar por que 2016 tinha 379 jogos (1 a menos que o padrão), foi identificado que se trata do acidente aéreo com a delegação da Chapecoense em novembro de 2016, dias antes da última rodada — o jogo Chapecoense x Internacional não foi realizado, em respeito às vítimas.

Verificado com filtro composto (& e |, já usados na Sprint 17):

jogos_chape_2016 = df.loc[
    (df["temporada"] == 2016) &
    ((df["mandante"] == "Chapecoense") | (df["visitante"] == "Chapecoense"))
]

print("Total de jogos da Chapecoense em 2016:", len(jogos_chape_2016))

Resultado: 37 jogos confirmados (38 rodadas − 1 partida não realizada), validando a integridade da coluna temporada e ilustrando como uma anomalia numérica pode carregar uma história real por trás — reforçando a importância de investigar, não apenas aceitar ou corrigir números sem entender a causa.

🔄 Migração completa: csv manual → Pandas

partidas.py — antes lia o CSV manualmente com csv.DictReader (Sprint 14) e devolvia uma lista de dicionários (partidas). Migrado para expor um DataFrame (df) já com todas as colunas auxiliares calculadas:

import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["ano"] = df["data"].dt.year

df["temporada"] = df["ano"]
df.loc[(df["ano"] == 2021) & (df["data"] <= "2021-02-25"), "temporada"] = 2020

df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]
df["empate"] = df["mandante_Placar"] == df["visitante_Placar"]
df["vitoria_visitante"] = df["mandante_Placar"] < df["visitante_Placar"]

Qualquer módulo que precisar desses dados agora faz from partidas import df, em vez de from partidas import partidas — e já recebe tudo pronto (temporada corrigida, colunas de resultado), sem recalcular nada.

main.py — reescrito para consultar o resumo de qualquer time (casa e fora) usando groupby() + agg(), calculados uma única vez fora do loop de consulta:

from partidas import df

resumo_mandante = df.groupby("mandante").agg(
    jogos=("mandante", "size"),
    vitorias=("vitoria_mandante", "sum"),
    empates=("empate", "sum"),
    derrotas=("vitoria_visitante", "sum")
)

resumo_visitante = df.groupby("visitante").agg(
    jogos=("visitante", "size"),
    empates=("empate", "sum"),
    vitorias=("vitoria_visitante", "sum"),
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

Pontos de atenção na migração:

resumo_mandante e resumo_visitante invertem o significado de "vitórias"/"derrotas" entre si: ao agrupar por visitante, vitoria_visitante representa a vitória do próprio time analisado, e vitoria_mandante representa a vitória do adversário (derrota do time analisado) — mesmo cuidado de nomenclatura já visto em sprints anteriores.
.loc[[time]] (colchete duplo) usado para preservar tipos numéricos corretos (evitar 386.0 em colunas que deveriam ser inteiras).
time not in resumo_mandante.index — .index de uma tabela agrupada por groupby() é a lista de categorias (nomes de time), usada para validar existência antes de consultar.

Teste final (Chapecoense): 132 jogos em casa, 133 fora — a diferença de 1 reflete exatamente o jogo não realizado contra o Internacional em 2016.

💡 Analogia (Excel)

.loc[condição, "coluna"] = valor é equivalente a usar "Localizar e Substituir" ou preencher manualmente uma coluna nova baseada em uma condição de filtro — mas aplicado de uma vez a todas as linhas que atendem a condição, sem precisar selecionar célula por célula.

📝 Anotações da Athena

Esta sprint uniu investigação de dados reais (não apenas cálculo) com uma migração estrutural importante do projeto. A correção da temporada 2020/2021 e a confirmação do caso Chapecoense mostraram, na prática, que anomalias numéricas em um dataset esportivo frequentemente refletem eventos reais (mudança de formato de campeonato, pandemia, tragédias) — investigar a causa antes de "corrigir cegamente" é uma habilidade central de análise de dados.

A migração de partidas.py e main.py para Pandas simplifica significativamente o código do Athena e centraliza toda a lógica de tratamento de dados (conversão de data, cálculo de temporada real, colunas de resultado) em um único lugar — qualquer nova funcionalidade do projeto poderá reaproveitar essas colunas sem duplicar cálculo algum.

Mudança de hábito adotada nesta sessão: destrinchar linha por linha todo código em Pandas por padrão, mesmo em sintaxes já vistas antes, para reforçar a fixação do raciocínio vetorizado/declarativo — diferente do estilo imperativo (for/if explícitos) das sprints anteriores.
