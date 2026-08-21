📘 Sprint 19 — Início da Fase 4: Estatística Aplicada (Média, Mediana, Desvio Padrão)
🎯 Objetivo

Iniciar a Fase 4 do roadmap (Estatística Aplicada ao Futebol), introduzindo mediana e desvio padrão como complementos à média, reorganizando estatisticas.py e main.py para restaurar a divisão de responsabilidades quebrada na migração da sessão anterior.

🔧 Reorganização estrutural (dívida técnica da migração para Pandas)

Depois da migração completa para Pandas (Sprint 18), o main.py havia acumulado lógica de cálculo direto nele (groupby().agg()), quebrando a divisão de responsabilidades estabelecida desde a Sprint 13. Além disso, estatisticas.py ainda continha funções antigas (manuais, com for/try/except), hoje obsoletas.

Correção: estatisticas.py passou a conter apenas funções reutilizáveis, e main.py voltou a ser apenas orquestração (importar, chamar, exibir).

def calcular_resumo_mandante(df):
    resumo = df.groupby("mandante").agg(
        jogos=("mandante", "size"),
        vitorias=("vitoria_mandante", "sum"),
        empates=("empate", "sum"),
        derrotas=("vitoria_visitante", "sum")
    )
    return resumo


def calcular_resumo_visitante(df):
    resumo = df.groupby("visitante").agg(
        jogos=("visitante", "size"),
        empates=("empate", "sum"),
        vitorias=("vitoria_visitante", "sum"),
        derrotas=("vitoria_mandante", "sum")
    )
    return resumo

📌 Analogia (Excel) para a divisão de responsabilidades

partidas.py é a aba "Dados" — dados brutos prontos. estatisticas.py é a aba "Fórmulas" — fórmulas genéricas (ex: =MÉDIA(?)) que não fazem nada sozinhas, só esperam ser apontadas para um intervalo. main.py é a aba "Resumo" — onde a fórmula é de fato aplicada a um intervalo real de dados, e o cálculo acontece. estatisticas.py não depende de partidas.py; apenas main.py depende dos dois, pois é ele quem conecta dado + fórmula.

🧠 Média, mediana e desvio padrão

Média sozinha pode enganar: dois conjuntos de dados podem ter a mesma média com comportamentos completamente diferentes (um consistente, outro instável). Mediana e desvio padrão complementam essa leitura.

def calcular_dispersao_gols(df, coluna):
    media = df[coluna].mean()
    mediana = df[coluna].median()
    desvio = df[coluna].std()

    return {
        "media": round(media, 2),
        "mediana": mediana,
        "desvio_padrao": round(desvio, 2)
    }

.mean(), .median(), .std() são métodos prontos do Pandas para qualquer coluna numérica. A função é genérica — recebe df e coluna como parâmetros, servindo tanto para mandante_Placar quanto visitante_Placar sem duplicar código.

📌 Parâmetros de função — reforço conceitual

coluna dentro da função é um "espaço reservado" (como uma célula de referência no Excel, ex: uma célula Z1 onde se digita o nome de uma coluna) que só recebe um valor real no momento da chamada. calcular_dispersao_gols(df, "mandante_Placar") e calcular_dispersao_gols(df, "visitante_Placar") usam a mesma função, escrita uma única vez, aplicada a colunas diferentes a cada chamada — mesmo princípio já visto com df e time em funções anteriores.

📊 Resultado — Brasileirão geral
Mandante: média 1.54, mediana 1.0, desvio padrão 1.23
Visitante: média 1.03, mediana 1.0, desvio padrão 1.03

Média (1.54) diferente da mediana (1.0) para o mandante indica distribuição assimétrica: a maioria dos jogos tem poucos gols (0 ou 1), mas jogos com goleadas ocasionais puxam a média para cima. Desvio padrão do mandante maior que o do visitante indica que o mandante tem resultados mais variados (mais "instabilidade") em quantidade de gols.

🎯 Dispersão de gols por time específico — composição de funções
def calcular_dispersao_gols_time(df, time):
    partidas_time = df.loc[df["mandante"] == time]
    return calcular_dispersao_gols(partidas_time, "mandante_Placar")

df.loc[df["mandante"] == time] filtra só as partidas em que aquele time foi mandante (operação vetorizada + filtro, já visto). A função reaproveita calcular_dispersao_gols já existente, passando o recorte filtrado no lugar do df completo — composição de funções, mesmo princípio da Sprint 12 (calcular_media_gols chamando calcular_total_gols).

Resultado — Palmeiras em casa: média 1.75, mediana 2.0, desvio padrão 1.28 (comparado ao geral do Brasileirão: média 1.54, mediana 1.0, desvio padrão 1.23) — o Palmeiras marca mais gols em casa que a média geral, e seu "jogo típico" já tem 2 gols (mediana), não 1.

📖 Como interpretar/narrar desvio padrão comparado à média

Desvio padrão mede a distância média entre os valores reais e a média. Regra prática (aproximada): a maioria dos valores tende a cair dentro do intervalo "média ± 1 desvio padrão".

Exemplo aplicado (Palmeiras em casa: média 1.75, desvio padrão 1.28): a faixa "normal" de gols por jogo fica entre aproximadamente 0 e 3 — jogos com 5-6 gols seriam exceções, não o padrão.

Regra geral para narrar o número: desvio padrão bem menor que a média → comportamento consistente e previsível; desvio padrão próximo ou maior que a média → comportamento instável, com variação considerável (indício de "jogos extremos" puxando a variação).

Analogia (Excel): duas colunas podem ter a mesma média (ex: [2,2,2,2,2] e [0,0,5,5,0], médias parecidas) mas aparências completamente diferentes num gráfico de dispersão — uma reta previsível, outra "saltando" — o desvio padrão quantifica essa diferença sem precisar olhar o gráfico.

📝 Anotações da Athena

Esta sprint marcou a entrada formal na Fase 4 do roadmap (Estatística Aplicada), com a introdução de mediana e desvio padrão como ferramentas de interpretação além da média simples. Também foi feita uma correção estrutural importante: a migração para Pandas da sessão anterior havia introduzido uma dívida técnica (lógica de cálculo vazando para main.py), corrigida restaurando a separação de responsabilidades entre dados (partidas.py), lógica de cálculo (estatisticas.py) e orquestração (main.py).

O ponto central da sprint, além do código, foi a interpretação: aprender a "contar uma história" a partir de média + desvio padrão juntos, em vez de olhar números isolados — habilidade que se conecta diretamente ao objetivo de transição de carreira para Ciência de Dados.

Próximos passos naturais: seguir explorando a Fase 4 (distribuições, porcentagens/probabilidades, correlação, desempenho casa x fora já formalizado estatisticamente, médias móveis, comparação entre equipes).
