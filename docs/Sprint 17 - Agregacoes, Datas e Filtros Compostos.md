📘 Sprint 17 — Agregações Avançadas, Datas e Filtros Compostos em Pandas
🎯 Objetivo

Aprofundar Pandas: combinar múltiplas agregações numa única chamada, trabalhar com datas, agrupar por mais de uma coluna, filtrar por condições compostas, e construir uma análise completa de confronto direto entre times.

🧠 agg() — múltiplas agregações de uma vez

Em vez de fazer um .groupby() separado para cada métrica, .agg() calcula várias colunas de resultado ao mesmo tempo, numa única passada pelos dados:

resumo_por_time = df.groupby("mandante").agg(
    jogos=("mandante", "size"),
    vitorias=("vitoria_mandante", "sum"),
    empates=("empate", "sum"),
    derrotas=("vitoria_visitante", "sum"),
    media_gols_marcados=("mandante_Placar", "mean"),
    media_gols_sofridos=("visitante_Placar", "mean")
).round(2)

Cada argumento define o nome da coluna de saída e, entre parênteses, qual coluna original usar + qual operação aplicar ("size", "sum", "mean"). .round(2) encadeado no final arredonda todas as colunas numéricas da tabela de uma vez.

📌 round() vs f-string para casas decimais

round(valor, 2) arredonda o valor de verdade (útil quando se quer arredondar várias colunas de uma tabela de uma vez). f"{valor:.2f}" só formata a exibição em um print() individual, sem alterar o valor guardado — mais útil ao imprimir um valor isolado dentro de uma frase.

⚠️ Series vs DataFrame de uma linha (dtype)

.loc[time] (colchete simples) devolve uma Series — que só aceita um tipo de dado para todos os valores, forçando inteiros a virarem float (ex: 386 vira 386.0) quando misturados com colunas decimais na mesma linha. .loc[[time]] (colchete duplo) devolve um DataFrame de uma linha só, onde cada coluna mantém seu próprio tipo — resolve o problema sem precisar formatar manualmente.

📅 Convertendo texto para data real
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["ano"] = df["data"].dt.year

pd.to_datetime() converte uma coluna de texto (ex: "29/03/2003") para o tipo datetime do Pandas. format="%d/%m/%Y" especifica explicitamente o formato original (dia/mês/ano), evitando interpretação errada. .dt é um acessador especial disponível só em colunas de data, liberando atributos como .year, .month, .day.

🗓️ groupby() com múltiplas colunas
evolucao_por_ano = df.groupby(["mandante", "ano"]).agg(
    jogos=("mandante", "size"),
    vitorias=("vitoria_mandante", "sum"),
    empates=("empate", "sum"),
    derrotas=("vitoria_visitante", "sum")
).round(2)

print(evolucao_por_ano.loc["Palmeiras"])

Passar uma lista de colunas para groupby() cria grupos mais finos (ex: por time E por ano). Com índice de duas camadas, .loc["Palmeiras"] já filtra só pelo time, devolvendo uma linha por ano.

⚠️ Anomalias históricas identificadas nos dados (contexto de domínio)

2003: início da era de pontos corridos no Brasileirão (antes havia mata-mata); Palmeiras estava na Série B nesse ano, por isso não aparece.
2013: mesma situação — Palmeiras rebaixado.
2004: 24 times na elite (23 jogos em casa). 2005: 22 times. A partir de 2006: 20 times, formato estável até hoje.
2020/2021: pandemia — o campeonato de 2020 só terminou em 2021, distorcendo a contagem de jogos por ano nesses dois anos.

Identificar esse tipo de anomalia (número de jogos fora do padrão) e investigar a causa real, em vez de aceitar cegamente, é uma etapa essencial de qualquer análise de dados. Fica registrado como ponto de atenção: tratamento futuro necessário para separar corretamente as partidas de 2020/2021 por temporada real.

🔍 Filtrando linhas por condição com .loc[]
df_recente = df.loc[df["ano"] >= 2022]

.loc[] também filtra linhas por condição booleana, não só busca por nome de índice. df["ano"] >= 2022 é uma operação vetorizada (como as comparações de placar), aplicada aqui contra um valor fixo em vez de outra coluna.

🔗 Combinando condições com & (e) e | (ou)
filtro = df.loc[(df["mandante"] == "Palmeiras") & (df["ano"] == 2016)]

Cada condição precisa ficar entre parênteses ao combinar com & ou |. & exige que todas as condições sejam verdadeiras; | exige que ao menos uma seja.

⚠️ Erro comum: comparar número com string vindo de input()

input() sempre devolve string, mesmo que a pessoa digite um número. Comparar df["ano"] (int) com ano (string, ex: "2016") nunca dá match — resulta em tabela vazia sem erro aparente. Corrigido convertendo: ano = int(input("Escolha o ano: ")).

🏆 Exercício final — Confronto direto entre dois times

Versão 1 (mandante e visitante fixos via input): reaproveita diretamente as colunas já existentes (vitoria_mandante, empate, vitoria_visitante), já que o time A sempre é mandante nesse filtro.

Versão 2 (mais avançada — nenhum dos dois times fixo como mandante):

confronto_geral = df.loc[
    ((df["mandante"] == time_a) & (df["visitante"] == time_b)) |
    ((df["mandante"] == time_b) & (df["visitante"] == time_a))
]

vitorias_a = (
    ((confronto_geral["mandante"] == time_a) & confronto_geral["vitoria_mandante"]) |
    ((confronto_geral["visitante"] == time_a) & confronto_geral["vitoria_visitante"])
).sum()

O filtro usa | para aceitar os dois sentidos possíveis do confronto (A em casa OU B em casa). O cálculo de "vitórias de A" exige lógica condicional composta: conta como vitória de A quando (A era mandante E o mandante venceu) OU (A era visitante E o visitante venceu) — porque, no confronto geral, vitoria_mandante sozinha não identifica mais quem é "A", já que A pode ter sido mandante ou visitante em cada partida.

Validação cruzada: a soma das vitórias/empates nas duas visões separadas (A em casa + B em casa) bateu exatamente com os totais do "confronto geral" (Palmeiras x Flamengo: 12 vitórias Palmeiras, 15 empates, 13 vitórias Flamengo, em 40 jogos desde 2003) — confirmando a lógica.

💡 Analogia (Excel)

.loc[condição] é equivalente a um filtro de coluna no Excel (as setinhas no cabeçalho, escolhendo "maior que X"). groupby() com múltiplas colunas é como uma Tabela Dinâmica com dois campos em "Linhas" (ex: Time e Ano).

📝 Anotações da Athena

Esta sprint consolidou Pandas como ferramenta de análise real: agregações combinadas, tratamento de datas, e filtros compostos com lógica condicional não trivial (o exercício de confronto direto exigiu pensar em duas perspectivas simultâneas — "quem é mandante" vs "quem é o time que queremos rastrear"). A identificação de anomalias históricas nos dados (mudança de formato do campeonato, pandemia) mostrou a importância de combinar conhecimento de domínio com análise de dados — um número "estranho" não é necessariamente um erro de código, pode refletir um evento real que precisa ser entendido antes de qualquer conclusão.

Próximos passos naturais: tratar as temporadas de 2020/2021 separadamente (mencionado como pendência), e seguir explorando Pandas ou avançar para a próxima fase do roadmap (Estatística aplicada ao futebol).
