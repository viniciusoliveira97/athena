📘 Sprint 21 — Fase 5: Visualização de Dados (Matplotlib e Plotly)
🎯 Objetivo

Iniciar a Fase 5 do roadmap (Visualização), aprofundando o uso do Matplotlib além do .plot() simples do Pandas, conhecendo o Plotly para gráficos interativos, e integrando ambos ao dashboard em Streamlit.

📊 Matplotlib — estrutura Figure e Axes

Até então, gráficos eram gerados via .plot() do próprio Pandas (um atalho simplificado). Nesta sprint, foi introduzida a estrutura real por trás do Matplotlib:

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(distribuicao_gols.index, distribuicao_gols.values, color="#2E7D32")

ax.set_title("Distribuição de gols do mandante", fontsize=14)
ax.set_xlabel("Gols")
ax.set_ylabel("Quantidade de jogos")

plt.show()

Destrinchamento:

plt.subplots() devolve dois objetos ao mesmo tempo: fig (a "folha" inteira, o quadro geral) e ax (os eixos — a área específica onde o gráfico é desenhado). Separados via atribuição múltipla, mesmo princípio já visto com col1, col2 = st.columns(2).
ax.bar(x, y, color=...) desenha o gráfico de barras nesse ax específico; color aceita código hexadecimal (mesmo sistema de cores personalizadas do Excel).
figsize=(largura, altura) controla o tamanho da figura em polegadas.
ax.set_title(), ax.set_xlabel(), ax.set_ylabel() adicionam título e rótulos aos eixos — importante para que o gráfico seja compreensível sozinho, sem explicação externa.
plt.show() abre a janela com o gráfico renderizado (imagem estática).

Analogia (Excel): fig é como a planilha inteira; ax é como um gráfico específico inserido dentro dela — uma planilha pode conter vários gráficos (vários ax).

🎲 Plotly — gráficos interativos

Instalação: pip install plotly (ou py -m pip install plotly, mesmo padrão de contorno de PATH já usado com streamlit).

import plotly.express as px

fig = px.bar(
    x=distribuicao_gols.index,
    y=distribuicao_gols.values,
    title="Distribuição de gols do mandante",
    labels={"x": "Gols", "y": "Quantidade de jogos"}
)

fig.show()

Diferente do Matplotlib (montado passo a passo com ax.bar(), depois ax.set_title(), etc.), o Plotly Express recebe todos os parâmetros de uma vez, como argumentos de uma única função (px.bar(...)). labels é um dicionário que renomeia os eixos (por padrão usariam literalmente "x" e "y"). fig.show() abre o gráfico em uma aba do navegador (via servidor local temporário), não em uma janela do sistema.

Vantagem central do Plotly: interatividade nativa — hover mostrando valores exatos ao passar o mouse, zoom por clique e arraste, ícones de reset/download — sem código adicional, diferente da imagem estática do Matplotlib.

🖥️ Integração no dashboard (app.py)

Gráfico de evolução por temporada, antes em st.bar_chart() (função simplificada do próprio Streamlit), substituído por Plotly:

import plotly.express as px

with aba_evolucao:
    st.subheader("Evolução de vitórias em casa por temporada")
    partidas_time = df.loc[df["mandante"] == time_escolhido]
    vitorias_por_temporada = partidas_time.groupby("temporada")["vitoria_mandante"].sum()

    fig = px.bar(
        x=vitorias_por_temporada.index,
        y=vitorias_por_temporada.values,
        labels={"x": "Temporada", "y": "Vitórias em casa"}
    )
    st.plotly_chart(fig, use_container_width=True)

st.plotly_chart(fig, ...) é a função do Streamlit específica para renderizar gráficos do Plotly, preservando toda a interatividade (diferente de st.bar_chart, que é mais simples). use_container_width=True ajusta o gráfico à largura disponível na tela.

📌 Decisão de escopo

Definido que aprofundamento em mais tipos de gráfico (linha, pizza, dispersão) e refinamento visual completo do dashboard ficam propositalmente para o final do projeto (Fase 10), quando a base analítica já estiver consolidada e for possível decidir com clareza quais métricas/visualizações merecem destaque. Referência de estilo definida para essa fase futura: Sofascore, BeSoccer e Packball.

📝 Anotações da Athena

Esta sprint deu o primeiro passo formal na Fase 5, cobrindo as duas ferramentas mencionadas no roadmap original (Matplotlib e Plotly) em um nível prático e comparativo: Matplotlib para controle fino e saídas estáticas (ex: relatórios, documentos), Plotly para interatividade e exploração (ex: dashboards). Ambas já foram testadas com dados reais do Brasileirão e integradas ao preview de dashboard em Streamlit.

A decisão de adiar o polimento visual completo para a Fase 10 reflete uma escolha consciente de priorização: consolidar a base analítica (Fases 3-4, e o restante do roadmap) antes de investir tempo em estética — evitando um dashboard bonito sem substância por trás.

Ideias de projeto futuras registradas nesta sessão: análise estatística de jogadores individuais (não apenas times), com exemplo de líder de desarmes em uma temporada específica de uma liga (ex: Dinamarca) — categoria mais ampla que as ideias de scouting já registradas anteriormente.
