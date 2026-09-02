📘 Sprint 25 — Fase 8: Índices de Força, Forma Recente e Elo Rating
🎯 Objetivo

Aprofundar a Fase 8 do roadmap (Analytics Avançado), construindo índices de força ofensiva/defensiva relativos à média da liga, forma recente (últimos N jogos), força ponderada de adversários, e implementação completa do Elo Rating — integrando tudo em uma nova aba "Confronto" no dashboard Streamlit.

📊 Índices de força ofensiva e defensiva
media_gols_liga = df["mandante_Placar"].mean()
media_gols_time = df.loc[df["mandante"] == "Palmeiras", "mandante_Placar"].mean()
indice_ofensivo = media_gols_time / media_gols_liga

Compara o desempenho de um time com a média da liga, em vez de olhar números absolutos. Índice > 1 = acima da média; < 1 = abaixo da média. Aplicado também à defesa (usando visitante_Placar como "gols sofridos" do mandante) — aqui a interpretação se inverte: quanto menor, melhor a defesa.

Formalizado como função reutilizável com parâmetros opcionais de temporada:

def calcular_indices_forca(df, time, temporada_inicio=None, temporada_fim=None):
    if temporada_inicio is not None:
        df = df.loc[df["temporada"] >= temporada_inicio]
    if temporada_fim is not None:
        df = df.loc[df["temporada"] <= temporada_fim]
    ...

Parâmetros com valor padrão None tornam o filtro de temporada opcional — chamando sem esses argumentos, a função usa o dataset inteiro. df.loc[condição, "coluna"] usado tanto para leitura (filtrar e já selecionar uma coluna) quanto revisitando o padrão de atribuição já visto na Sprint 18.

Resultado (Palmeiras): índices gerais (22 anos) de 1.14 ofensivo / 0.97 defensivo, versus índices recentes (2020-2024) de 1.32 ofensivo / 0.85 defensivo — evidenciando uma melhora real e mensurável do time nos últimos anos, não uma ilusão de poucos jogos.

🔁 Forma recente com .apply()
partidas_palmeiras = df.loc[df["mandante"] == "Palmeiras"].sort_values("data")
ultimos_5_jogos = partidas_palmeiras.tail(5)

def classificar_resultado(linha):
    if linha["vitoria_mandante"]:
        return "V"
    elif linha["empate"]:
        return "E"
    else:
        return "D"

ultimos_5_jogos["resultado"] = ultimos_5_jogos.apply(classificar_resultado, axis=1)

.sort_values("data") + .tail(n) recupera os últimos n jogos em ordem cronológica. .apply(funcao, axis=1) aplica uma função personalizada a cada linha do DataFrame (axis=1 = linha por linha), necessário quando a lógica depende de várias colunas simultaneamente — diferente das operações vetorizadas simples usadas até então. Observação de performance: .apply() é mais lento que vetorização pura, aceitável em recortes pequenos mas a evitar em datasets grandes quando uma alternativa vetorizada existir.

🥊 Força ponderada de adversários

Ao calcular a força média dos 19 adversários que um time enfrentou em uma temporada inteira, o resultado tende matematicamente a ~1.0 (média da liga), já que em pontos corridos todo time enfrenta todos os outros — uma limitação metodológica identificada na prática. Repetindo o cálculo apenas para os últimos 5 jogos (não a temporada inteira), o resultado passa a ser informativo de verdade, respondendo perguntas como "a sequência recente de resultados aconteceu contra adversários fáceis ou difíceis?".

♟️ Elo Rating — conceito e implementação

Conceito: em vez de tratar a força de um time como fixa dentro de um período, o Elo trata como uma crença que se refina a cada partida, ajustando-se proporcionalmente à surpresa do resultado (vitória esperada muda pouco o rating; resultado surpreendente muda muito). Resolve a limitação da contagem simples de vitórias, que trata "vencer o líder" e "vencer o lanterna" como equivalentes.

Fórmula da expectativa (probabilidade de vitória do mandante, baseada na diferença de rating):

expectativa_mandante = 1 / (1 + 10 ** ((rating_visitante - rating_mandante) / 400))

O divisor 400 é uma constante de calibração histórica do sistema Elo (praticamente sempre fixa entre implementações). Resultado sempre entre 0 e 1 — uma probabilidade.

Fórmula de atualização pós-jogo:

novo_rating = rating + K * (resultado_real - expectativa)

resultado_real - expectativa é o "erro de previsão": positivo quando o resultado superou a expectativa, negativo quando ficou abaixo, com magnitude proporcional à surpresa. K é um fator de sensibilidade ajustável (diferente do 400): K alto reage rápido a resultados recentes mas é mais instável; K baixo é mais estável mas lento para refletir mudanças reais. Usado K=30, valor comum na literatura de futebol.

Implementação completa no dataset (~8785 partidas), percorridas em ordem cronológica:

df_ordenado = df.sort_values("data")
ratings = {}

for _, partida in df_ordenado.iterrows():
    mandante = partida["mandante"]
    visitante = partida["visitante"]
    rating_mandante = ratings.get(mandante, 1500)
    rating_visitante = ratings.get(visitante, 1500)
    expectativa_mandante = 1 / (1 + 10 ** ((rating_visitante - rating_mandante) / 400))
    ...
    ratings[mandante] = novo_rating_mandante
    ratings[visitante] = novo_rating_visitante

.iterrows() percorre um DataFrame linha por linha (necessário aqui porque cada resultado depende do estado — rating — deixado pelas partidas anteriores, diferente de operações vetorizadas independentes por linha). ratings.get(time, 1500) busca o rating atual de um time no dicionário, usando 1500 como valor padrão para times aparecendo pela primeira vez.

Resultado (ranking Elo atual, top 5): Botafogo-RJ (1730), Palmeiras (1693), Flamengo (1682), Corinthians (1663), Internacional (1662) — coerente com o futebol brasileiro recente (Botafogo campeão 2024), demonstrando a sensibilidade do Elo a resultados recentes mais do que a tradição histórica isolada.

🖥️ Integração no dashboard — nova aba "Confronto"

Cálculo de Elo encapsulado em função com cache:

@st.cache_data
def calcular_elo(k=30, rating_inicial=1500):
    ...
    return ratings

@st.cache_data é um decorator do Streamlit — calcula a função uma vez e reutiliza o resultado em reruns subsequentes, evitando reprocessar as ~8785 partidas a cada interação do usuário (já que o Streamlit reroda o script inteiro a cada clique).

Nova aba permite escolher dois times (dois st.selectbox com key diferentes, necessário para múltiplos seletores na mesma página), exibindo Elo de cada um, probabilidade de vitória calculada pela fórmula de expectativa, e histórico de confrontos diretos reaproveitando o filtro construído na Sprint 17.

📌 Curiosidade relacionada: Tukey Fences (detecção de outliers)

Discutido conceito de "cercas" estatísticas (Q1 - 1.5×IQR e Q3 + 1.5×IQR para outliers potenciais; ×3 para extremos), conectando com a investigação manual já feita na Sprint 18 (identificação do jogo não realizado da Chapecoense em 2016) — um método formal para o mesmo tipo de desconfiança de dado "fora do padrão" já praticada intuitivamente.

💬 Reflexões pessoais registradas na sessão

Discutida a origem do interesse do usuário em Ciência de Dados: anos de experiência escrevendo prognósticos manuais de apostas esportivas, combinando análise estatística (probabilidade implícita, valor de odds, histórico de confrontos, splits casa/fora) com contexto qualitativo (lesões e substitutos, estilo do técnico, clima, motivação) — já possuía o raciocínio analítico, faltavam as ferramentas de escala. Também discutido o cenário de mercado de trabalho (Data Engineering crescendo em remuneração e demanda mais que Data Science em 2026, papéis complementares e não hierárquicos), reforçando que o roadmap do Athena já cobre bem os dois lados (estatística e engenharia/SQL/banco).

📝 Anotações da Athena

Esta sprint representa um salto de sofisticação analítica real: de índices simples relativos à média, passando por forma recente com lógica condicional por linha (.apply()), até um sistema de rating dinâmico e amplamente usado na indústria (Elo), tudo já integrado a uma interface interativa. A limitação identificada na força de adversários (tendência a 1.0 em amostra completa da temporada) é um exemplo valioso de raciocínio metodológico maduro — testar um método e reconhecer quando ele não traz informação nova é tão importante quanto aplicá-lo corretamente.

Próximos passos naturais: expandir a aba de Confronto com os índices de força ofensiva/defensiva e forma recente já construídos, e seguir explorando Fase 8 (por exemplo, comparação sistemática entre equipes, ou refinamentos do Elo).
