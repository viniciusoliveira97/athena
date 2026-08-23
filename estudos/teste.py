import sys
sys.path.append("src")

from partidas import df
import plotly.express as px

distribuicao_gols = df["mandante_Placar"].value_counts().sort_index()

fig = px.bar(
    x=distribuicao_gols.index,
    y=distribuicao_gols.values,
    title="Distribuição de gols do mandante",
    labels={"x": "Gols", "y": "Quantidade de jogos"}
)

fig.show()