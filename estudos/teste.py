import sqlite3

conexao = sqlite3.connect("data/athena.db")

resultado = conexao.execute("""
    SELECT mandante, COUNT(*) as jogos, SUM(vitoria_mandante) as vitorias
    FROM partidas
    GROUP BY mandante
    ORDER BY vitorias DESC
    LIMIT 5
""")

for linha in resultado:
    print(linha)

conexao.close() 