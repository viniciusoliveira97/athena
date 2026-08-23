import streamlit as st
import sys
import plotly.express as px

sys.path.append("src")

from partidas import df
from estatisticas import (
    calcular_resumo_mandante,
    calcular_resumo_visitante,
    calcular_dispersao_gols_time,
    calcular_tabela_over,
)

st.set_page_config(
    page_title="Athena — Brasileirão",
    page_icon="⚽",
    layout="wide",
)

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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Jogos em casa", int(linha_casa["jogos"]))
col2.metric("Vitórias em casa", int(linha_casa["vitorias"]))
col3.metric("Empates em casa", int(linha_casa["empates"]))
col4.metric("Derrotas em casa", int(linha_casa["derrotas"]))

aba_resumo, aba_dispersao, aba_probabilidades, aba_evolucao = st.tabs(
    ["📋 Resumo", "📈 Dispersão de gols", "🎲 Probabilidades", "🗓️ Evolução por temporada"]
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
