import streamlit as st
import sys

sys.path.append("src")

from partidas import df
from estatisticas import (
    calcular_resumo_mandante,
    calcular_resumo_visitante,
    calcular_dispersao_gols_time,
    calcular_tabela_over,
)
import plotly.express as px

st.set_page_config(
    page_title="Athena — Brasileirão",
    page_icon="⚽",
    layout="wide",
)


@st.cache_data
def calcular_elo(k=30, rating_inicial=1500):
    df_ordenado = df.sort_values("data")

    ratings = {}

    for _, partida in df_ordenado.iterrows():
        mandante = partida["mandante"]
        visitante = partida["visitante"]

        rating_mandante = ratings.get(mandante, rating_inicial)
        rating_visitante = ratings.get(visitante, rating_inicial)

        expectativa_mandante = 1 / (1 + 10 ** ((rating_visitante - rating_mandante) / 400))

        if partida["vitoria_mandante"]:
            resultado_mandante = 1
        elif partida["empate"]:
            resultado_mandante = 0.5
        else:
            resultado_mandante = 0

        novo_rating_mandante = rating_mandante + k * (resultado_mandante - expectativa_mandante)
        novo_rating_visitante = rating_visitante + k * ((1 - resultado_mandante) - (1 - expectativa_mandante))

        ratings[mandante] = novo_rating_mandante
        ratings[visitante] = novo_rating_visitante

    return ratings


ratings_elo = calcular_elo()

resumo_mandante = calcular_resumo_mandante(df)
resumo_visitante = calcular_resumo_visitante(df)

times = sorted(resumo_mandante.index.tolist())

with st.sidebar:
    st.title("⚽ Athena")
    st.caption("Preview do Dashboard — Fase 10 do roadmap")
    time_escolhido = st.selectbox("Escolha um time:", times)

st.header(time_escolhido)

linha_casa = resumo_mandante.loc[time_escolhido]
linha_fora = resumo_visitante.loc[time_escolhido]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Jogos em casa", int(linha_casa["jogos"]))
col2.metric("Vitórias em casa", int(linha_casa["vitorias"]))
col3.metric("Empates em casa", int(linha_casa["empates"]))
col4.metric("Derrotas em casa", int(linha_casa["derrotas"]))
col5.metric("Elo atual", round(ratings_elo[time_escolhido], 1))

aba_resumo, aba_dispersao, aba_probabilidades, aba_evolucao, aba_confronto = st.tabs(
    ["📋 Resumo", "📈 Dispersão de gols", "🎲 Probabilidades", "🗓️ Evolução por temporada", "⚔️ Confronto"]
)

with aba_resumo:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"{time_escolhido} em casa")
        st.dataframe(resumo_mandante.loc[[time_escolhido]])

    with col2:
        st.subheader(f"{time_escolhido} fora")
        st.dataframe(resumo_visitante.loc[[time_escolhido]])

with aba_dispersao:
    st.subheader("Dispersão de gols em casa")
    dispersao = calcular_dispersao_gols_time(df, time_escolhido)
    col1, col2, col3 = st.columns(3)
    col1.metric("Média", dispersao["media"])
    col2.metric("Mediana", dispersao["mediana"])
    col3.metric("Desvio padrão", dispersao["desvio_padrao"])

with aba_probabilidades:
    st.subheader(f"Probabilidades de over — {time_escolhido} em casa")
    partidas_time_casa = df.loc[df["mandante"] == time_escolhido]
    tabela_over = calcular_tabela_over(partidas_time_casa)
    st.table(tabela_over)

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

with aba_confronto:
    st.subheader("Confronto direto")

    col1, col2 = st.columns(2)
    with col1:
        time_a = st.selectbox("Time A (casa):", times, key="time_a")
    with col2:
        time_b = st.selectbox("Time B (fora):", times, index=1, key="time_b")

    if time_a == time_b:
        st.warning("Escolha dois times diferentes.")
    else:
        elo_a = ratings_elo[time_a]
        elo_b = ratings_elo[time_b]

        expectativa_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

        col1, col2, col3 = st.columns(3)
        col1.metric(f"Elo {time_a}", round(elo_a, 1))
        col2.metric(f"Elo {time_b}", round(elo_b, 1))
        col3.metric(f"Chance de vitória de {time_a} (casa)", f"{expectativa_a:.1%}")

        confronto = df.loc[(df["mandante"] == time_a) & (df["visitante"] == time_b)]

        if len(confronto) == 0:
            st.info("Esses dois times nunca se enfrentaram com esse mando de campo.")
        else:
            st.subheader(f"Histórico: {time_a} (casa) x {time_b} (fora)")
            vitorias_a = confronto["vitoria_mandante"].sum()
            empates_confronto = confronto["empate"].sum()
            vitorias_b = confronto["vitoria_visitante"].sum()

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Jogos", len(confronto))
            col2.metric(f"Vitórias {time_a}", int(vitorias_a))
            col3.metric("Empates", int(empates_confronto))
            col4.metric(f"Vitórias {time_b}", int(vitorias_b))