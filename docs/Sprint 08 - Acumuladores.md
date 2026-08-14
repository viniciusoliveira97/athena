Resumo da Sprint 8 — Acumuladores
O que você aprendeu
O que é um acumulador.
A diferença entre contador e acumulador.
Como percorrer uma lista de dicionários e somar valores.
Que apenas acessar um valor:
partida["gols_mandante"]

não produz nenhum efeito se você não fizer nada com ele.

Como atualizar um acumulador:
total_gols_mandante = total_gols_mandante + partida["gols_mandante"]
A importância da indentação: colocar um print() dentro do for ou fora dele muda completamente o comportamento do programa.
Um destaque da aula

Houve um momento que achei muito importante.

Quando perguntei quanto valia:

partida["gols_mandante"]

você respondeu:

1, 2 e 3.

Depois percebemos juntos que você estava confundindo:

o valor da partida atual;
com o valor do acumulador.

Essa distinção é fundamental. Depois que ela ficou clara, você conseguiu escrever o acumulador praticamente sozinho.

Esse tipo de ajuste de raciocínio é exatamente o que faz alguém evoluir em programação.

Avaliação

Eu diria que hoje você teve um desempenho excelente.

Você não ficou esperando respostas prontas. Em vários momentos, parou para pensar e corrigiu o código por conta própria. Esse é o comportamento que queremos desenvolver durante todo o projeto Athena.