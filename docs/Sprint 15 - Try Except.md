📘 Sprint 15 — Tratamento de Erros (try/except)
🎯 Objetivo

Aprender a lidar com dados "sujos" ou inesperados (arquivo com valor vazio, texto onde deveria ter número) sem que o programa quebre inteiro, e eliminar duplicação de código entre funções parecidas.

🧠 Conceito principal

Até aqui, qualquer erro de conversão (ex: int("") ou int("adiado")) travava o programa inteiro com um ValueError, mesmo que fosse só 1 linha problemática em milhares de partidas boas.

try/except resolve isso: "tenta fazer isso; se der erro, faz aquilo outro em vez de quebrar tudo."

try:
    gols_mandante = int(partida["mandante_Placar"])
except ValueError:
    print("Valor inválido:", partida["mandante_Placar"])

O que está dentro de try: é o que você quer que aconteça. Se der erro em qualquer linha dentro do try, o Python pula direto pro except: em vez de travar o programa. ValueError é o erro específico que o Python lança ao tentar converter algo pra número e o conteúdo não ser válido — capturar o erro específico (em vez de qualquer erro) evita esconder problemas que deveriam aparecer.

💻 Aplicando com contador de erros e continue
def contar_vitorias_mandante(partidas):
    vitorias_mandante = 0
    partidas_com_erro = 0

    for partida in partidas:
        try:
            gols_mandante = int(partida["mandante_Placar"])
            gols_visitante = int(partida["visitante_Placar"])
        except ValueError:
            partidas_com_erro = partidas_com_erro + 1
            continue

        if gols_mandante > gols_visitante:
            vitorias_mandante = vitorias_mandante + 1

    print("Partidas com erro:", partidas_com_erro)
    return vitorias_mandante

O continue dentro do except pula pra próxima partida do for sem tentar comparar gols que não existem (por terem falhado na conversão).

⚠️ Problema identificado: duplicação de código

A mesma lógica de try/except + conversão foi repetida em três funções (contar_vitorias_mandante, contar_empates, contar_vitorias_visitante), cada uma percorrendo a lista inteira de partidas separadamente só para decidir uma coisa diferente no final. Rodando as três, "Partidas com erro: 0" aparecia repetido três vezes no terminal — sinal de trabalho duplicado.

🔧 Refatoração: uma função única com if/elif/else

Como cada partida só pode ser vitória do mandante, empate ou vitória do visitante (nunca mais de uma), as três decisões podem ser feitas dentro do mesmo loop, com uma única passada pelos dados:

def calcular_estatisticas(partidas):
    vitorias_mandante = 0
    empates = 0
    vitorias_visitante = 0
    partidas_com_erro = 0

    for partida in partidas:
        try:
            gols_mandante = int(partida["mandante_Placar"])
            gols_visitante = int(partida["visitante_Placar"])
        except ValueError:
            partidas_com_erro = partidas_com_erro + 1
            continue

        if gols_mandante > gols_visitante:
            vitorias_mandante = vitorias_mandante + 1
        elif gols_mandante == gols_visitante:
            empates = empates + 1
        else:
            vitorias_visitante = vitorias_visitante + 1

    return {
        "vitorias_mandante": vitorias_mandante,
        "empates": empates,
        "vitorias_visitante": vitorias_visitante,
        "partidas_com_erro": partidas_com_erro,
    }

📌 Novidade: return de um dicionário com múltiplos valores

Até esta sprint, toda função devolvia um único valor com return. Agora a função devolve várias informações de uma vez, organizadas como um dicionário — cada resultado ganha um nome (chave), evitando confusão sobre qual número é qual.

main.py consumindo o resultado:

from partidas import partidas
from estatisticas import calcular_estatisticas

resultado = calcular_estatisticas(partidas)

print("Vitórias do mandante:", resultado["vitorias_mandante"])
print("Empates:", resultado["empates"])
print("Vitórias do visitante:", resultado["vitorias_visitante"])
print("Partidas com erro:", resultado["partidas_com_erro"])

O dicionário devolvido é acessado do mesmo jeito que já era feito com partida["mandante_Placar"].

🏆 Resultado final (Brasileirão 2003–2022, dataset completo)
Vitórias do mandante: 4359
Empates: 2321
Vitórias do visitante: 2105
Partidas com erro: 0

Soma bate exatamente com o total de partidas do dataset (8785), e zero erros de conversão — o CSV está limpo nesse quesito.

💡 Analogia (Excel)

try/except é parecido com a função SEERRO() do Excel: =SEERRO(fórmula; "valor alternativo"). Se a fórmula principal falhar (ex: dividir por zero), o Excel mostra um valor alternativo em vez de #DIV/0! espalhado pela planilha. A diferença é que em Python o "o que fazer se der erro" é um bloco de código inteiro, não só um valor de substituição.

📝 Anotações da Athena

Esta sprint trouxe dois aprendizados que vão além da sintaxe: lidar com dados reais exige prever que eles podem vir incompletos ou inválidos (try/except), e perceber quando código está sendo repetido desnecessariamente entre funções parecidas é sinal de que existe uma forma mais organizada de resolver o problema (refatoração para calcular_estatisticas).

A troca de "três funções, um valor cada" por "uma função, um dicionário com vários valores" é um padrão que vai se repetir bastante no Athena — principalmente quando começarem relatórios e dashboards, que consomem justamente esse tipo de resultado estruturado.
