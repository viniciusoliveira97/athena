📘 Sprint 22 — Início da Fase 6: Banco de Dados e SQL (SQLite)
🎯 Objetivo

Iniciar a Fase 6 do roadmap, introduzindo o conceito de banco de dados relacional, criando o primeiro banco SQLite do Athena, e aprendendo os comandos SQL básicos (SELECT, WHERE, GROUP BY, ORDER BY, LIMIT), comparando cada um com seu equivalente já dominado em Pandas.

🧠 Por que banco de dados, além de CSV

Até esta sprint, o Athena relia o CSV inteiro toda vez que rodava. Banco de dados resolve isso com: melhor performance em buscas específicas, estrutura relacional (dados organizados em tabelas conectadas, em vez de uma única tabela "achatada"), e é o padrão usado em sistemas profissionais.

Escolha de engine: SQLite — embutido no próprio Python (módulo sqlite3, sem necessidade de pip install), guarda tudo em um único arquivo local. Ideal para projetos pessoais sem necessidade de servidor, diferente de PostgreSQL ou MySQL.

Decisão de escopo: iniciar com uma única tabela (partidas), replicando a estrutura atual do df, adiando a divisão em múltiplas tabelas relacionadas (campeonatos → temporadas → times → partidas → estatisticas, conforme o roadmap original) para sprints futuras — esse processo de dividir dados em tabelas relacionadas se chama normalização.

💻 Criando o banco de dados a partir do DataFrame
import sqlite3
import sys

sys.path.append("src")

from partidas import df

conexao = sqlite3.connect("data/athena.db")

df.to_sql("partidas", conexao, if_exists="replace", index=False)

conexao.close()

Destrinchamento:

sqlite3.connect("data/athena.db") cria (ou abre) um arquivo de banco de dados — pode conter várias tabelas dentro dele.
df.to_sql("partidas", conexao, ...) grava o DataFrame como uma tabela chamada "partidas" dentro do banco. if_exists="replace" recria a tabela do zero a cada execução (evita duplicação ao rodar de novo); index=False evita salvar o índice numérico do Pandas como coluna.
conexao.close() libera a conexão com o arquivo após o uso.

Analogia (Excel): equivalente a um "Salvar como", levando dados que estavam na memória (DataFrame) para um arquivo permanente, só que em formato de banco de dados em vez de planilha.

🔍 Consultando com SQL — SELECT e WHERE
resultado = conexao.execute("""
    SELECT mandante, visitante, mandante_Placar, visitante_Placar
    FROM partidas
    WHERE mandante = 'Palmeiras'
    LIMIT 5
""")

for linha in resultado:
    print(linha)

SELECT colunas FROM tabela — seleciona colunas específicas (equivalente a df[["col1", "col2"]] no Pandas); usar * seleciona todas as colunas. WHERE condição filtra linhas (equivalente a df.loc[condição]) — texto em SQL usa aspas simples ('Palmeiras'), diferente do Python. LIMIT n restringe a quantidade de linhas retornadas (equivalente a .head(n)).

Observação sobre o formato do resultado: cada linha retornada por SQL puro vem como uma tupla, sem nomes de coluna visíveis (diferente do Pandas, que rotula automaticamente) — mais parecido com a leitura manual de CSV anterior ao uso de DictReader (Sprint 14).

📊 Agregação com GROUP BY
resultado = conexao.execute("""
    SELECT mandante, COUNT(*) as jogos, SUM(vitoria_mandante) as vitorias
    FROM partidas
    GROUP BY mandante
    ORDER BY vitorias DESC
    LIMIT 5
""")

COUNT(*) conta linhas por grupo (equivalente a "size" no .agg()). SUM(coluna) soma valores por grupo (equivalente a .sum()). as apelido nomeia a coluna calculada (equivalente aos nomes definidos em .agg(nome=(...))). GROUP BY coluna agrupa por valor (equivalente a df.groupby()). ORDER BY coluna DESC ordena do maior para o menor (equivalente a .sort_values(ascending=False)).

Resultado validado: ranking de vitórias em casa (São Paulo, Internacional, Flamengo, Santos, Athletico-PR) bateu com os times "grandes" já conhecidos de análises anteriores em Pandas.

📋 Tabela comparativa Pandas × SQL
Pandas                                          SQL
df.loc[df["mandante"] == "Palmeiras"]           WHERE mandante = 'Palmeiras'
df.groupby("mandante")                          GROUP BY mandante
.agg(vitorias=("col", "sum"))                   SUM(col) as vitorias
.sort_values("vitorias", ascending=False)       ORDER BY vitorias DESC
.head(5)                                        LIMIT 5
📌 Decisão de escopo

JOIN (comando SQL para combinar múltiplas tabelas relacionadas) foi conscientemente adiado para quando a estrutura do banco evoluir para múltiplas tabelas — aprender no contexto de necessidade real, em vez de memorizar sem aplicação imediata.

📝 Anotações da Athena

Esta sprint iniciou a Fase 6 do roadmap com uma abordagem comparativa: cada comando SQL novo foi apresentado lado a lado com seu equivalente já dominado em Pandas, reforçando que a lógica de "filtrar, agrupar, ordenar, limitar" é a mesma independente da ferramenta — só a sintaxe muda. Essa comparação é uma habilidade valiosa para o mercado de trabalho, já que muitos sistemas armazenam dados diretamente em bancos SQL, exigindo consultas diretas sem sempre poder trazer tudo para um DataFrame primeiro.

O banco de dados athena.db já existe fisicamente no projeto (pasta data/), com a tabela partidas espelhando os dados do CSV processado. Próximos passos naturais: seguir explorando SQL conforme a necessidade (incluindo JOIN quando houver múltiplas tabelas), e eventualmente evoluir a estrutura para o modelo relacional completo sugerido no roadmap original (campeonatos, temporadas, times, partidas, estatisticas).
