📘 Sprint 14 — Leitura de Arquivos CSV
🎯 Objetivo

Trazer dados reais para o Athena, substituindo listas fictícias por um dataset real do Brasileirão, lido diretamente de um arquivo CSV.

🧠 Conceito principal

Um CSV é uma planilha sem formatação: só texto, valores separados por vírgula, onde a primeira linha é o cabeçalho (nomes das colunas). É o mesmo tipo de dado que uma planilha do Excel gera "por trás" quando salva em .csv.

Python tem um módulo pronto para ler isso, o csv:

import csv

with open("data/campeonato-brasileiro-full.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
        break

csv.DictReader lê o cabeçalho e usa os nomes das colunas como chaves de dicionário — cada linha do arquivo já chega pronta como um dicionário, no mesmo formato que já vínhamos usando manualmente (partida["chave"]).

💻 Lendo o arquivo inteiro de uma vez

DictReader só percorre o arquivo uma vez, linha por linha. Para guardar tudo como uma lista de dicionários (igual já era feito manualmente), usamos list():

with open("data/campeonato-brasileiro-full.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    partidas = list(leitor)

Depois disso, partidas é uma lista de dicionários normal — as funções escritas na Sprint 12 não precisam mudar de estrutura, só se adaptar aos nomes reais das colunas.

⚠️ Diferenças entre dados fictícios e dados reais

1. Nomes de coluna diferentes

O dataset real usa mandante_Placar e visitante_Placar, não gols_mandante e gols_visitante como nos exercícios anteriores.

2. Tudo chega como texto (string), até números

'mandante_Placar': '4' é uma string "4", não o número 4. Comparar strings numéricas funciona por acaso com 1 dígito, mas quebra com números maiores (ex: "10" > "9" dá errado, porque compara caractere por caractere). É preciso converter com int() antes de comparar — mesma lógica do int(input(...)) da Sprint 11.

3. encoding="utf-8"

Todo arquivo de texto é salvo como uma sequência de bytes, e o encoding é a regra usada para transformar esses bytes em caracteres legíveis (letras, acentos). Especificar encoding="utf-8" explicitamente garante que acentos e caracteres especiais (nomes de times como "São Paulo", "Grêmio") sejam lidos corretamente, independente do sistema operacional. Sem isso, acentos podem sair corrompidos.

🏆 Funções adaptadas para dados reais

Em estatisticas.py:

def contar_vitorias_mandante(partidas):
    vitorias_mandante = 0

    for partida in partidas:
        gols_mandante = int(partida["mandante_Placar"])
        gols_visitante = int(partida["visitante_Placar"])

        if gols_mandante > gols_visitante:
            vitorias_mandante = vitorias_mandante + 1

    return vitorias_mandante


def contar_empates(partidas):
    empates = 0

    for partida in partidas:
        gols_mandante = int(partida["mandante_Placar"])
        gols_visitante = int(partida["visitante_Placar"])

        if gols_mandante == gols_visitante:
            empates = empates + 1

    return empates


def contar_vitorias_visitante(partidas):
    vitorias_visitante = 0

    for partida in partidas:
        gols_mandante = int(partida["mandante_Placar"])
        gols_visitante = int(partida["visitante_Placar"])

        if gols_mandante < gols_visitante:
            vitorias_visitante = vitorias_visitante + 1

    return vitorias_visitante

Resultado rodando sobre o dataset completo (Brasileirão 2003–2022, +8000 partidas):

Vitórias do mandante: 4359
Empates: 2321
Vitórias do visitante: (restante do total)

🗂️ Organização em módulos (reforço da Sprint 13)

partidas.py → só dados: abre o CSV, lê, expõe a lista partidas. Nenhuma função de cálculo deve estar aqui.

import csv

with open("data/campeonato-brasileiro-full.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    partidas = list(leitor)

estatisticas.py → só lógica de cálculo (as três funções acima).

main.py → importa dos dois e executa:

from partidas import partidas
from estatisticas import contar_vitorias_mandante, contar_empates, contar_vitorias_visitante

vitorias = contar_vitorias_mandante(partidas)
empates = contar_empates(partidas)
vitorias_visitante = contar_vitorias_visitante(partidas)

print("Vitórias do mandante:", vitorias)
print("Empates:", empates)
print("Vitórias do visitante:", vitorias_visitante)

⚠️ Erro comum cometido e corrigido nesta sprint

Função de cálculo (contar_vitorias_mandante) foi colada por engano dentro de partidas.py, duplicando o que já existia em estatisticas.py, além de uma chamada de teste solta (resultado = ...) sem uso real. Corrigido removendo a função e a linha solta de partidas.py, mantendo cada arquivo com sua responsabilidade única.

💡 Analogia (Excel)

DictReader + list() é como um "Selecionar tudo + Copiar" da planilha inteira de uma vez, transformando cada linha em um registro (dicionário) pronto para uso — em vez de ler célula por célula manualmente.

O problema de encoding é o mesmo que acontece às vezes ao abrir um .csv no Excel e os acentos aparecerem bugados (ex: "AtlÃ©tico" em vez de "Atlético") — resolvido escolhendo a codificação certa na importação, assim como especificamos encoding="utf-8" no open() do Python.

📝 Anotações da Athena

Esta sprint marcou a virada de dados fictícios para dados reais: o Athena rodou pela primeira vez suas funções de estatística sobre um dataset real do Brasileirão (2003–2022, +8000 partidas), obtido de um repositório open-source no GitHub.

A estrutura de módulos da Sprint 13 se provou útil na prática: como main.py e estatisticas.py não dependem de como os dados chegam, foi possível trocar a fonte de dados (de lista fictícia para CSV real) sem precisar alterar a lógica de cálculo — só os nomes das chaves e a conversão para int().

Fecha-se aqui a Fase 2 inicial (engenharia básica do Athena). Próximos passos naturais: seguir explorando o dataset real (outras métricas, times específicos) e, mais adiante no roadmap, migrar a leitura de dados para Pandas (Fase 3).
