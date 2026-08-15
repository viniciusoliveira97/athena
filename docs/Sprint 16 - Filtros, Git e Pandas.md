📘 Sprint 16 — Filtros Avançados, Git/GitHub e Introdução ao Pandas
Cobre: filtros avançados por time, input interativo, Git/GitHub, e introdução ao Pandas. (Sprint condensada — reúne o fechamento da Sprint 15 na prática com a primeira exploração da Fase 3 do roadmap.)

🎯 Contexto

Depois da Sprint 15 (try/except e eliminação de duplicação com calcular_estatisticas), o Athena evoluiu em três frentes: filtros mais realistas por time (casa/fora, com input do usuário), controle de versão com Git/GitHub, e a entrada na Fase 3 do roadmap com Pandas.

🏆 Parte 1 — Filtros por time (casa e fora)
Filtrando partidas por mandante e visitante

Duas funções simétricas em filtros.py:

def filtrar_partidas_mandante(partidas, time):
    partidas_do_time = []

    for partida in partidas:
        if partida["mandante"] == time:
            partidas_do_time.append(partida)

    return partidas_do_time


def filtrar_partidas_visitante(partidas, time):
    partidas_do_time = []

    for partida in partidas:
        if partida["visitante"] == time:
            partidas_do_time.append(partida)

    return partidas_do_time

📌 append()

Método que adiciona um item ao final de uma lista existente, modificando ela diretamente (diferente de recriar um valor, como no acumulador total = total + gol). Sintaxe: lista.append(item) — o ponto antes do nome indica que é um método, uma ação pertencente especificamente a listas.

Analogia (Excel): como preencher uma coluna sempre na próxima linha vazia, empilhando valores no final.

📌 Operador % (módulo/resto)

Devolve o resto de uma divisão. numero % 2 == 0 verifica se um número é par (resto 0 na divisão por 2). Equivalente à função MOD() do Excel: =MOD(7;2) → 1.

Comparando desempenho casa x fora (Palmeiras, Santos, Cruzeiro)

Composição de funções: filtrar_partidas_mandante/visitante devolve uma lista no mesmo formato de sempre, que é passada direto para calcular_estatisticas (Sprint 15), sem precisar alterar essa última.

Resultados obtidos:

Palmeiras: 58% de vitórias em casa vs 33% fora
Santos: 56% de vitórias em casa vs 27% fora
Cruzeiro: em casa 198V/92E/81D em 371 jogos; fora 120V/83E/168D

Confirma o "fator casa" do futebol brasileiro de forma mensurável, e mostra que alguns times dependem mais do mando de campo que outros.

⚠️ Cuidado com nomenclatura ao inverter contexto

Ao analisar o time como visitante, as chaves do dicionário de calcular_estatisticas ficam "invertidas" em relação ao significado: resultado_fora["vitorias_visitante"] representa as vitórias do time analisado, e resultado_fora["vitorias_mandante"] representa as vitórias do adversário (ou seja, derrota do time analisado).

Input interativo com validação e loop

Uso de input() para escolher o time, com verificação de existência (lista vazia = time não encontrado) e while True para permitir múltiplas consultas seguidas:

while True:
    time = input("Escolha o time para analisar (ou 'sair' para encerrar): ")

    if time == "sair":
        break

    partidas_casa = filtrar_partidas_mandante(partidas, time)
    partidas_fora = filtrar_partidas_visitante(partidas, time)

    if len(partidas_casa) == 0:
        print("Time não encontrado. Verifique o nome digitado.")
    else:
        resultado_casa = calcular_estatisticas(partidas_casa)
        resultado_fora = calcular_estatisticas(partidas_fora)
        # ... prints dos resultados

print("Programa encerrado.")

Checar só partidas_casa é suficiente para validar o time — no Brasileirão, todo time que disputa a Série A joga tanto em casa quanto fora, então não há necessidade de checar as duas listas.

🗂️ Parte 2 — Git e GitHub
Conceito

Git funciona em "fotografias" do projeto ao longo do tempo (commits), cada uma com uma mensagem explicando o que mudou. Roda localmente no computador. GitHub é um serviço online que hospeda repositórios Git na nuvem — funciona como backup remoto e permite portfólio público.

Comandos essenciais usados
git init                                    # inicia o repositório (uma vez só por projeto)
git config --global user.name "..."         # configura nome (uma vez por computador)
git config --global user.email "..."        # configura e-mail (uma vez por computador)
git status                                  # mostra o que mudou
git add .                                   # inclui todas as mudanças no próximo commit
git commit -m "mensagem"                    # cria a fotografia (commit)
Removendo __pycache__ do controle de versão

__pycache__/ é uma pasta gerada automaticamente pelo Python (cache interno), não deve ser versionada. Adicionada ao .gitignore, e removida do rastreamento já existente sem apagar do disco:

git rm -r --cached src/__pycache__
git add .
git commit -m "Remove __pycache__ do controle de versão"
Subindo para o GitHub

Repositório criado no site do GitHub (sem inicializar com README/gitignore, para evitar conflito com o que já existia localmente). Conectado e enviado com:

git remote add origin https://github.com/USUARIO/athena.git
git branch -M main
git push -u origin main

Repositório publicado com sucesso em github.com/viniciusoliveira97/athena, com histórico de commits e toda a estrutura do projeto (src/, data/, docs/, estudos/).

💡 Analogia (Excel)

Git é como salvar cópias nomeadas de uma planilha antes de mudanças arriscadas, mas de forma organizada e com histórico completo guardado dentro do próprio projeto.

📊 Parte 3 — Introdução ao Pandas (Fase 3 do roadmap)
Instalação
pip install pandas
DataFrame e leitura de CSV

Um DataFrame é a estrutura principal do Pandas — equivalente a uma planilha inteira carregada na memória (linhas, colunas, cabeçalho).

import pandas as pd

df = pd.read_csv("data/campeonato-brasileiro-full.csv")

print(df.head())

pd.read_csv() substitui inteiro o bloco manual de csv.DictReader + list() usado na Sprint 14. df.head() mostra as 5 primeiras linhas. [5 rows x 16 columns] no rodapé é metadado — informação sobre a tabela (quantidade de linhas/colunas), não um dado da tabela em si.

Encoding padrão

Por padrão, read_csv() assume UTF-8 se nenhum encoding for especificado — por isso não foi necessário passar encoding="utf-8" manualmente como na Sprint 14. Se o arquivo estiver em outra codificação (ex: latin-1), pode ser especificado com pd.read_csv("arquivo.csv", encoding="latin-1").

Operações vetorizadas

Comparar ou operar colunas inteiras de uma vez, sem for explícito:

vitorias_mandante = (df["mandante_Placar"] > df["visitante_Placar"]).sum()
empates = (df["mandante_Placar"] == df["visitante_Placar"]).sum()
vitorias_visitante = (df["mandante_Placar"] < df["visitante_Placar"]).sum()

df["mandante_Placar"] > df["visitante_Placar"] compara as duas colunas linha a linha, gerando uma nova coluna de True/False. Como True vale 1 e False vale 0, .sum() conta quantos True existem. Resultados bateram exatamente com o cálculo manual: 4359 vitórias do mandante, 2321 empates, 2105 vitórias do visitante.

Analogia (Excel): equivalente a arrastar uma fórmula (=G2>H2) por uma coluna inteira, só que instantâneo.

Médias e criação de colunas
media_gols_mandante = df["mandante_Placar"].mean()
df["total_gols"] = df["mandante_Placar"] + df["visitante_Placar"]
media_gols_partida = df["total_gols"].mean()

.mean() calcula a média de uma coluna diretamente. df["nova_coluna"] = ... cria uma coluna nova a partir de outras, também de forma vetorizada. Resultado: média de 2.56 gols por partida no Brasileirão histórico.

Formatação de números com f-string
print(f"Média de gols por partida: {media_gols_partida:.2f}")

f antes das aspas cria uma f-string, permitindo inserir variáveis dentro do texto com {}. :.2f formata como float com 2 casas decimais. Formata só a exibição, sem alterar a precisão do valor guardado — equivalente à formatação de exibição de uma célula no Excel.

groupby() — agrupamento por categoria
df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]

vitorias_por_time = df.groupby("mandante")["vitoria_mandante"].sum().sort_values(ascending=False)

groupby("mandante") agrupa todas as linhas pelo valor da coluna mandante (uma partida por time, em grupos). ["vitoria_mandante"] seleciona a coluna de interesse dentro de cada grupo. .sum() soma os True de cada grupo (conta vitórias). .sort_values(ascending=False) ordena do maior para o menor.

Analogia (Excel): equivalente a uma Tabela Dinâmica, com um campo em "Linhas" e outro em "Valores" com agregação de contagem/soma.

Encadeamento de métodos: cada .algumacoisa() recebe o resultado do anterior e aplica mais uma operação, como uma linha de produção. Pode ser escrito também em etapas separadas para maior clareza durante o aprendizado.

.loc[] e .index

Para acessar um valor específico de uma Series pelo nome (rótulo):

vitorias_por_time.loc["Palmeiras"]

Para checar se um nome existe entre os rótulos (substituindo a checagem de lista vazia usada com filtros manuais):

if time in vitorias_por_time.index:

Combinando com input()

Todas as métricas (vitórias, empates, derrotas) calculadas uma única vez com groupby() fora do loop de consulta — mais eficiente que recalcular a cada nova consulta, diferente da abordagem manual anterior:

df["vitoria_mandante"] = df["mandante_Placar"] > df["visitante_Placar"]
df["empate"] = df["mandante_Placar"] == df["visitante_Placar"]
df["vitoria_visitante"] = df["mandante_Placar"] < df["visitante_Placar"]

vitorias_por_time = df.groupby("mandante")["vitoria_mandante"].sum()
empates_por_time = df.groupby("mandante")["empate"].sum()
derrotas_por_time = df.groupby("mandante")["vitoria_visitante"].sum()

time = input("Escolha o time para analisar: ")

if time in vitorias_por_time.index:
    print(f"--- {time} em casa ---")
    print("Vitórias:", vitorias_por_time.loc[time])
    print("Empates:", empates_por_time.loc[time])
    print("Derrotas:", derrotas_por_time.loc[time])
else:
    print("Time não encontrado. Verifique o nome digitado.")

📝 Anotações da Athena

Esse bloco marcou três avanços importantes: (1) ferramentas de consulta mais realistas e interativas, aplicando composição de funções e tratamento de erro em um caso de uso completo; (2) a adoção de controle de versão (Git/GitHub), com o Athena publicado como repositório público — um passo relevante para o objetivo de portfólio na transição de carreira; e (3) a entrada na Fase 3 do roadmap com Pandas, onde ficou evidente o valor de já entender a lógica manual por trás de cada operação (filtro, contagem, média, agrupamento) antes de usar a versão abstraída pela biblioteca.

O padrão que se repete: Pandas não substitui o raciocínio já desenvolvido nas sprints anteriores — ele resume código repetitivo (loops, contadores, comparações manuais) em chamadas de método, mantendo a mesma lógica por trás.

Próximo passo natural: seguir explorando Pandas (mais estatísticas agregadas, possivelmente comparações entre temporadas) e, no momento oportuno, considerar migrar o main.py do Athena para usar Pandas no lugar do módulo csv manual.
