📘 Sprint 7 — Contadores
🎯 Objetivo

Aprender a contar quantas vezes um evento acontece durante um for.

🧠 Conceito principal

Um contador é uma variável que começa em zero e aumenta normalmente de 1 em 1.

Exemplo:

contador = 0

contador = contador + 1
contador = contador + 1
contador = contador + 1

print(contador)

Saída:

3
📌 Quando usar?

Sempre que a pergunta começar com:

Quantos...
Quantas...
Número de...

Exemplos:

Quantas vitórias?
Quantos empates?
Quantos clientes?
Quantos gols acima de 3?
Quantas partidas terminaram 0x0?
💻 Estrutura básica
contador = 0

for item in lista:

    if condição:
        contador = contador + 1
🏆 Exemplo da Sprint
vitorias_mandante = 0
empates = 0
vitorias_visitante = 0

for partida in partidas:

    if partida["gols_mandante"] > partida["gols_visitante"]:
        vitorias_mandante = vitorias_mandante + 1

    elif partida["gols_mandante"] == partida["gols_visitante"]:
        empates = empates + 1

    else:
        vitorias_visitante = vitorias_visitante + 1
⚠️ Erros comuns
Colocar lógica dentro do dicionário.
Esquecer de inicializar o contador.
Atualizar o contador errado (empates em vez de vitorias_visitante, por exemplo).
💡 Analogia

Imagine uma folha de papel.

Cada vez que acontece uma vitória do mandante, você faz um risquinho.

|
||
|||

O contador faz exatamente isso, mas usando números.

📝 Anotações da Athena

Contador = contar acontecimentos.

Começa em 0.

Normalmente soma 1.

É usado quando queremos saber quantas vezes algo aconteceu.