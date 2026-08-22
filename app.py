import streamlit as st
import sys

sys.path.append("src")

from partidas import df
from estatisticas import calcular_resumo_mandante, calcular_resumo_visitante, calcular_dispersao_gols_time

st.title("Athena — Preview do Dashboard")
st.write("Uma prévia da Fase 10 do roadmap, usando os dados e funções que já existem no projeto.")

resumo_mandante = calcular_resumo_mandante(df)
resumo_visitante = calcular_resumo_visitante(df)

times = sorted(resumo_mandante.index.tolist())

time_escolhido = st.selectbox("Escolha um time:", times)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{time_escolhido} em casa")
    st.dataframe(resumo_mandante.loc[[time_escolhido]])

with col2:
    st.subheader(f"{time_escolhido} fora")
    st.dataframe(resumo_visitante.loc[[time_escolhido]])

st.subheader("Dispersão de gols em casa")
dispersao = calcular_dispersao_gols_time(df, time_escolhido)
st.write(dispersao)

st.subheader("Evolução de vitórias em casa por temporada")
partidas_time = df.loc[df["mandante"] == time_escolhido]
vitorias_por_temporada = partidas_time.groupby("temporada")["vitoria_mandante"].sum()
st.bar_chart(vitorias_por_temporada)
