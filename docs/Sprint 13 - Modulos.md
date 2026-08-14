📘 Sprint 13 — Separar Código em Arquivos e Módulos
🎯 Objetivo

Aprender a dividir o projeto em vários arquivos (módulos), em vez de manter tudo em um único arquivo .py, preparando o Athena para crescer sem virar uma bagunça.

🧠 Conceito principal

Um módulo é, na prática, qualquer arquivo .py — ele pode ter funções e variáveis que outros arquivos importam e reutilizam.

Em vez de:

login
cadastro de partidas
cálculo de estatísticas
geração de relatórios

tudo dentro de um único arquivo gigante, cada responsabilidade ganha seu próprio arquivo, e um arquivo principal (main.py) importa e orquestra tudo.

💻 Estrutura usada no Athena

estatisticas.py → lógica de cálculo (funções)

def contar_vitorias_mandante(partidas):
    vitorias_mandante = 0

    for partida in partidas:
        if partida["gols_mandante"] > partida["gols_visitante"]:
            vitorias_mandante = vitorias_mandante + 1

    return vitorias_mandante


def contar_empates(partidas):
    empates = 0

    for partida in partidas:
        if partida["gols_mandante"] == partida["gols_visitante"]:
            empates = empates + 1

    return empates

partidas.py → dados

partidas = [
    {"gols_mandante": 2, "gols_visitante": 1},
    {"gols_mandante": 0, "gols_visitante": 0},
    {"gols_mandante": 1, "gols_visitante": 3},
    {"gols_mandante": 4, "gols_visitante": 2},
]

main.py → executa, juntando tudo

from partidas import partidas
from estatisticas import contar_vitorias_mandante, contar_empates

vitorias = contar_vitorias_mandante(partidas)
empates = contar_empates(partidas)

print("Vitórias do mandante:", vitorias)
print("Empates:", empates)

📌 Sintaxe do import
from nome_do_arquivo import nome_da_funcao_ou_variavel

nome_do_arquivo é o nome do arquivo .py sem a extensão .py. Os arquivos precisam estar na mesma pasta (por enquanto — subpastas/pacotes é assunto mais avançado).

⚠️ Import circular

Acontece quando dois arquivos tentam importar um do outro (direta ou indiretamente), criando um loop sem fim. O Python detecta e lança erro.

Exemplo do que evitar:

# estatisticas.py
from relatorio import gerar_relatorio

# relatorio.py
from estatisticas import contar_empates

Regra prática: pensar na direção das dependências como uma escada, sempre em um único sentido — dados → cálculo → relatório/exibição. Um módulo "de baixo" (ex: estatisticas.py, só cálculo) nunca deve importar um módulo "de cima" (ex: relatorio.py, que usa os cálculos prontos). No Athena: partidas.py → estatisticas.py → main.py, sem nenhum importar de volta.

⚠️ Caminhos relativos dependem de onde o comando é executado

Um erro comum: rodar python src/main.py estando na raiz do projeto pode gerar ModuleNotFoundError, porque o Python procura os módulos a partir da pasta onde o comando foi executado, não da pasta onde o arquivo está salvo.

Solução usada: entrar na pasta antes de rodar.

cd src
python main.py

(Existem formas mais avançadas de resolver isso com pacotes, mas ficam para mais à frente.)

💡 Analogia (Excel)

partidas.py é como uma aba de dados brutos (uma aba "Base", uma linha por partida). estatisticas.py é como fórmulas em células separadas (tipo =CONT.SE() ou =SOMASE()) que leem a aba de dados e calculam um número. relatorio.py seria uma aba de resumo/dashboard, que usa o resultado das fórmulas para montar texto ou visual — nunca recalcula do zero.

O import circular é o primo direto da "referência circular" do Excel: nos dois casos, a regra é a mesma — dados → cálculo → apresentação, numa única direção, nunca de volta.

📝 Anotações da Athena

Esta sprint marcou a transição de "um único arquivo" para uma estrutura de projeto de verdade, com responsabilidades separadas por arquivo — mesma ideia de "responsabilidade única" aprendida na Sprint 12 para funções, agora aplicada a módulos inteiros.

O Athena já tinha uma estrutura de pastas planejada anteriormente (data/, docs/, estudos/, notebooks/, src/, tests/), e as funções de estatística e a lista de partidas foram organizadas dentro de src/, junto aos módulos já existentes.

Essa organização se mostrou útil imediatamente na Sprint 14, quando foi possível trocar a fonte de dados (de lista fictícia para CSV real) sem alterar a lógica de cálculo — só main.py e partidas.py precisaram mudar.
