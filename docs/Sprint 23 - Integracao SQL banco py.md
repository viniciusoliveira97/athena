📘 Sprint 23 — Integração de SQL ao Projeto (banco.py)
🎯 Objetivo

Integrar o banco de dados SQLite de forma organizada à estrutura de módulos do Athena, criando um arquivo dedicado (banco.py) e conectando-o ao fluxo existente (partidas.py, main.py), com consultas seguras e resultados devolvidos como DataFrame.

🗂️ Novo módulo: src/banco.py
import sqlite3
import pandas as pd

CAMINHO_BANCO = "data/athena.db"


def criar_banco(df):
    conexao = sqlite3.connect(CAMINHO_BANCO)
    df.to_sql("partidas", conexao, if_exists="replace", index=False)
    conexao.close()


def buscar_partidas_time(time):
    conexao = sqlite3.connect(CAMINHO_BANCO)

    consulta = "SELECT * FROM partidas WHERE mandante = ?"
    resultado = pd.read_sql_query(consulta, conexao, params=(time,))

    conexao.close()
    return resultado

Destrinchamento:

CAMINHO_BANCO — variável em maiúsculas (convenção para "constante"), centralizando o caminho do arquivo do banco em um único lugar, evitando repetição em várias funções.
criar_banco(df) — encapsula a gravação do DataFrame no banco (já testada na Sprint 22), agora reutilizável como função.
pd.read_sql_query(consulta, conexao, params=(...)) — diferente de conexao.execute() (que devolve tuplas cruas), essa função do Pandas executa a consulta SQL e já devolve o resultado como DataFrame, com nomes de coluna — juntando o melhor dos dois mundos (SQL para a consulta, Pandas para manipular o resultado).

📌 Parâmetros de consulta (query parameters) — segurança

WHERE mandante = ? junto com params=(time,) é a forma seg­ura de inserir um valor variável em uma consulta SQL. O ? é um espaço reservado que o Pandas/SQLite preenche de forma segura com o valor de params, evitando SQL Injection — uma vulnerabilidade onde texto malicioso inserido em uma consulta poderia manipular ou danificar o banco caso o valor fosse colado diretamente dentro do texto SQL. Prática recomendada mesmo em projetos pessoais, para consolidar o hábito correto desde já.

🔄 Sincronização automática do banco

Adicionado ao final de partidas.py:

from banco import criar_banco

criar_banco(df)

Garante que o banco athena.db é recriado automaticamente a partir dos dados mais atuais toda vez que partidas.py é importado (ou seja, toda vez que o Athena roda) — eliminando o risco de o banco ficar desatualizado em relação ao CSV/DataFrame processado.

✅ Validação

Testado buscar_partidas_time("Palmeiras") — resultado com 386 partidas, batendo exatamente com o número já validado anteriormente via filtro direto em Pandas (df.loc[df["mandante"] == "Palmeiras"]). Confirma que os dois caminhos (Pandas puro e consulta SQL via banco) chegam ao mesmo resultado, sendo o Athena agora capaz de consultar dados por qualquer um dos dois métodos.

⚠️ Lembrete recorrente de estrutura de pastas

Reforçado (mais uma vez) que testes em estudos/teste.py precisam de sys.path.append("src") para importar módulos de src/, já que o Python busca módulos a partir da pasta onde o comando foi executado, não da pasta onde o arquivo de teste está salvo.

📝 Anotações da Athena

Esta sprint consolidou a integração de SQL ao projeto de forma organizada, seguindo o mesmo princípio de responsabilidade única já aplicado desde a Sprint 13: banco.py cuida exclusivamente de conexão e consultas ao banco de dados, sem se misturar com a lógica de cálculo estatístico (estatisticas.py) ou orquestração (main.py).

O uso de parâmetros de consulta (?  + params) introduziu um conceito de segurança relevante para qualquer trabalho futuro com bancos de dados, reforçando que boas práticas valem a pena mesmo em projetos pessoais sem múltiplos usuários.

Próximos passos naturais: expandir banco.py com mais funções de consulta conforme a necessidade (ex: buscar por temporada, por confronto direto), e, mais adiante no roadmap, evoluir a estrutura para múltiplas tabelas relacionadas — momento em que JOIN se tornará necessário.
