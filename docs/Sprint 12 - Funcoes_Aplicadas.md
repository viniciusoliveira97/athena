📘 Sprint 12 — Funções Aplicadas
🎯 Objetivo

Aplicar tudo que já foi aprendido (contadores, acumuladores, listas, dicionários, for, if) dentro de funções reais, transformando lógica solta em blocos reutilizáveis.

🧠 Conceito principal

Até a Sprint 10, as funções eram pequenas, só para aprender a sintaxe (def, parâmetros, return).

Na Sprint 12, o objetivo passou a ser outro: pegar programas que já sabíamos escrever soltos e organizá-los dentro de funções, com responsabilidade clara.

Exemplo de responsabilidade de função:

def calcular_total_gols(gols_mandante, gols_visitante):
    return gols_mandante + gols_visitante

Receber dois valores e devolver a soma — fácil de explicar em uma frase. Essa é a marca de uma boa função.

💻 Função recebendo lista + acumulador + return
def calcular_total_gols(lista_gols):
    total = 0

    for gol in lista_gols:
        total = total + gol

    return total

Aqui a função:

recebe uma lista como parâmetro;
percorre com for;
acumula com total;
devolve o resultado com return.

🔗 Composição de funções

Uma função pode chamar outra função. Isso foi um marco importante da sprint.

def calcular_media_gols(lista_gols):
    total = calcular_total_gols(lista_gols)
    quantidade = len(lista_gols)

    media = total / quantidade

    return media

calcular_media_gols() reaproveita calcular_total_gols() em vez de repetir a lógica de soma.

📌 len()

len() devolve quantos elementos existem em uma lista.

gols = [2, 1, 3, 0, 4]
len(gols)  # 5
🏆 Exercício da Sprint — contar vitórias do mandante
def contar_vitorias_mandante(partidas):
    vitorias_mandante = 0

    for partida in partidas:
        if partida["gols_mandante"] > partida["gols_visitante"]:
            vitorias_mandante = vitorias_mandante + 1

    return vitorias_mandante

Testado com uma lista de 4 partidas → resultado correto: 2 vitórias do mandante.

🏆 Exercício da Sprint — contar empates
def contar_empates(partidas):
    empates = 0

    for partida in partidas:
        if partida["gols_mandante"] == partida["gols_visitante"]:
            empates = empates + 1

    return empates

Escrita corretamente na primeira tentativa, já aplicando todos os pontos da correção anterior.

⚠️ Erros comuns (cometidos e corrigidos durante a sprint)

if fora do for por indentação errada — o if de decisão precisa estar identado dentro do for.
Contador não inicializado antes do for — vitorias_mandante = 0 precisa existir antes do loop começar.
return dentro do if, no meio do loop — isso encerra a função na primeira ocorrência e devolve None. O return do resultado final só deve acontecer depois que o for termina de percorrer tudo.
else: break dentro do for — interrompe o loop inteiro na primeira partida que não bate a condição, fazendo a função ignorar as partidas seguintes. Quando não há nada a fazer no else, basta omiti-lo.
Confundir print com return — print apenas exibe na tela; return devolve o valor para quem chamou a função, permitindo reutilização.

💡 Analogia

Uma função com return é como uma calculadora: você entrega os números (parâmetros), ela processa por dentro, e devolve o resultado pronto para você usar em outra conta. Uma função com apenas print é como um cartaz: mostra a informação, mas você não pode "pegar" o valor de volta.

📝 Anotações da Athena

A Sprint 12 marcou a transição de "aprender sintaxe de função" para "organizar programas reais em funções". A composição de funções (uma função chamando outra) é o padrão que vai sustentar o Athena daqui em diante — cada função pequena resolve uma parte específica, e funções maiores orquestram as menores.

Duas funções ficaram prontas e reutilizáveis para o projeto:

contar_vitorias_mandante(partidas)
contar_empates(partidas)

Seguindo o mesmo padrão, contar_vitorias_visitante(partidas) sai quase pronta (basta trocar > por < na comparação) — fica como próximo exercício natural.

Este mini-projeto marca o fechamento da Fase 1 (Fundamentos de Python) do roadmap do Athena. A Sprint 13 inicia a Fase 2 — Athena começa a nascer, com separação de código em módulos e, na sequência (Sprint 14), leitura de dados reais via CSV.
