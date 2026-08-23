📘 Sprint 20 — Correlação, Distribuição de Frequência e Probabilidade/Odds
🎯 Objetivo

Continuar a Fase 4 (Estatística Aplicada) explorando correlação entre variáveis, distribuição de frequência (com primeiro contato com Matplotlib), e probabilidade aplicada a odds de apostas — tudo já integrado ao dashboard em Streamlit.

🔗 Correlação
correlacao = df["mandante_Placar"].corr(df["visitante_Placar"])

.corr() calcula o coeficiente de correlação de Pearson entre duas colunas numéricas — mede se duas variáveis "andam juntas" (positiva), "andam ao contrário" (negativa), ou não têm relação linear (perto de zero). Resultado sempre entre -1 e +1.

Como o cálculo funciona na prática: para cada linha, calcula o desvio de cada valor em relação à própria média, multiplica os dois desvios entre si, soma tudo, e divide pelos desvios padrão das duas colunas. Se os valores "andam juntos" (ambos acima ou ambos abaixo da média), os produtos tendem a ser positivos e a soma cresce; se andam ao contrário, os produtos tendem a ser negativos.

Resultados obtidos e comparados:

Gols do mandante × Gols do visitante: 0.045 (praticamente nula) — hipóteses de jogo "aberto" (correlação positiva) e "efeito goleada" (correlação negativa) se cancelam no agregado.
Gols do mandante × Vitória do mandante: 0.61 (forte) — esperado, mas não perfeito porque vitória depende da comparação com o placar do adversário (ex: 2x2 não é vitória apesar de 2 gols).
Saldo de gols (mandante − visitante) × Vitória do mandante: 0.79 (muito forte) — uma métrica derivada, combinando os dois lados da partida numa única informação, capturou a relação de forma mais precisa que os gols do mandante isolados.

📊 Distribuição de frequência
distribuicao_gols = df["mandante_Placar"].value_counts().sort_index()

.value_counts() conta quantas vezes cada valor único aparece na coluna; .sort_index() reordena pelo próprio valor (0, 1, 2...) em vez de pela frequência. Analogia (Excel): equivalente a uma Tabela Dinâmica com o campo em "Linhas" e "Contagem" em "Valores".

Resultado (gols do mandante): distribuição com pico em 1 gol (3008 partidas) e cauda longa decrescente até 7 gols (7 partidas) — um formato chamado assimetria positiva / cauda à direita, que explica por que a média (1.54) é maior que a mediana (1.0): poucos jogos com muitos gols puxam a média para cima sem representar o "jogo típico".

Mesma análise aplicada ao total de gols da partida (mandante + visitante): pico em 2 gols, cauda estendendo-se até 11 gols (1 partida em ~8785).

Visualização com Matplotlib (instalado via pip install matplotlib):

distribuicao_gols.plot(kind="bar")

import matplotlib.pyplot as plt
plt.show()

.plot() é um método do Pandas que usa Matplotlib por baixo; plt.show() abre a janela com o gráfico renderizado.

📌 Observação conectada a Machine Learning futuro

O formato da distribuição observada (pico baixo, cauda longa, contagem de eventos raros) é característico da distribuição de Poisson, usada para modelar "quantas vezes um evento ocorre em um intervalo" — relevante para a Fase 8 do roadmap (modelos de gols) e mencionado também como base conceitual para um projeto futuro de portfólio (fora do Athena) analisando dados públicos da Uber.

🎲 Probabilidade e odds
probabilidade_vitoria_mandante = df["vitoria_mandante"].mean()

Média de uma coluna booleana (True/False) é matematicamente igual à proporção de True — ou seja, a probabilidade daquele evento. Resultado: 49.6% (bate com os números já conhecidos: 4359 vitórias mandante em 8785 jogos).

Odd justa (sem margem):

odd_justa = 1 / probabilidade_vitoria_mandante

Odd com margem da casa (juice/vig):

odd_com_juice = odd_justa * (1 - margem_casa)

Multiplicar pela margem é equivalente ao cálculo de desconto (ex: preço com 5% de desconto = preço × 0.95). Pesquisa confirmou que a margem real de casas de apostas no Brasil para futebol fica entre 4% e 10%, dependendo da liquidez do mercado — o valor de exemplo usado (5%) está bem alinhado com a prática real. O termo técnico usado pelo mercado para essa margem é overround; o cálculo real de uma casa aplicaria a margem simultaneamente às três probabilidades do mercado (vitória mandante, empate, vitória visitante), não apenas a uma isolada.

Probabilidade de over/under, aplicada de forma genérica e reutilizável
def calcular_probabilidade_over(df, linha=2.5):
    total_gols = df["mandante_Placar"] + df["visitante_Placar"]
    return (total_gols > linha).mean()

Introduz o conceito de valor padrão de parâmetro: linha=2.5 permite chamar a função sem especificar a linha (assume 2.5), ou sobrescrever passando outro valor.

Resultado geral (Brasileirão): 47.3% de chance de over 2.5 gols — odd justa correspondente: 2.115.

Probabilidade condicional (por time/contexto): reforçando que uma probabilidade "de tabela" (geral) não reflete o comportamento específico de cada situação — vários fatores (time, mando de campo, momento de temporada, confronto direto, etc.) alteram a probabilidade real de um evento. Testado com Palmeiras em casa: 51.0% de over 2.5 (vs. 47.3% geral) — diferença que confirma a hipótese, na prática, usando o mesmo tipo de filtro (df.loc[df["mandante"] == time]) já usado em sprints anteriores.

Tabela de múltiplas linhas de over, formatada como porcentagem:

def calcular_tabela_over(df):
    linhas = [0.5, 1.5, 2.5, 3.5]

    probabilidades = {}
    for linha in linhas:
        chave = f"over {linha}"
        valor = calcular_probabilidade_over(df, linha)
        probabilidades[chave] = f"{valor:.2%}"

    return probabilidades

Percorre uma lista de linhas com for, reaproveitando calcular_probabilidade_over a cada iteração, montando um dicionário com chaves tipo "over 0.5" e valores já formatados como texto em porcentagem (f"{valor:.2%}", 2 casas decimais).

🖥️ Integração com o dashboard (app.py)

Adicionada seção de probabilidades de over por time escolhido, reaproveitando o selectbox já existente:

st.subheader(f"Probabilidades de over — {time_escolhido} em casa")

partidas_time_casa = df.loc[df["mandante"] == time_escolhido]
tabela_over = calcular_tabela_over(partidas_time_casa)

st.write(tabela_over)

⚠️ Erro corrigido nesta sessão

Dentro de calcular_tabela_over, uma chamada recursiva acidental (calcular_tabela_over(df, linha) em vez de calcular_probabilidade_over(df, linha)) causou TypeError, já que a função só aceitava um argumento. Corrigido apontando para a função correta dentro do loop.

📝 Anotações da Athena

Esta sprint consolidou três pilares de estatística aplicada — correlação, distribuição de frequência e probabilidade — todos testados com dados reais e imediatamente integrados ao preview de dashboard em Streamlit, reforçando o ciclo de aprendizado: teoria em Pandas → validação no terminal → visualização interativa.

Um fio condutor importante emergiu nesta sessão: a diferença entre probabilidade incondicional (geral, "de tabela") e probabilidade condicional (considerando contexto específico — time, mando de campo, confronto direto). Isso conecta diretamente com interesses pessoais already registrados (análise de odds e apostas esportivas) e aponta para direções futuras do roadmap (Fase 8 — modelos de gols com Poisson, cálculo de odds justas com as três probabilidades do mercado simultaneamente).

Próximos passos naturais: seguir explorando Fase 4 (se desejado) ou avançar para Fase 5 (visualização — já iniciada informalmente com o gráfico de distribuição em Matplotlib).
