# Sprint 11 - Estruturas de Repetição (`while`)

## Objetivo

Aprender a utilizar o `while` para repetir instruções enquanto uma condição for verdadeira.

Nesta sprint também foram estudados:

- `input()`
- conversão com `int()`
- operador `!=`
- loops infinitos
- `break`
- `continue`
- variáveis de controle
- integração entre repetição, condições e acumuladores

---

# 1. O que é o while?

O `while` é uma estrutura de repetição.

Ele executa um bloco de código enquanto determinada condição for `True`.

Exemplo:

```python
contador = 1

while contador <= 3:
    print(contador)
    contador = contador + 1
```

Saída:

```text
1
2
3
```

O funcionamento é:

1. O Python verifica a condição.
2. Se for `True`, entra no `while`.
3. Executa as instruções identadas.
4. Volta ao início.
5. Verifica novamente a condição.
6. Quando a condição for `False`, encerra o `while`.

---

# 2. Diferença entre for e while

O `for` normalmente é utilizado quando percorremos uma coleção ou temos uma sequência definida.

Exemplo:

```python
for partida in partidas:
    print(partida)
```

O `while` é útil quando a repetição depende de uma condição.

Exemplo:

```python
while senha_digitada != senha_correta:
```

Não sabemos necessariamente quantas tentativas serão necessárias.

---

# 3. Alterando a condição do while

É importante que alguma coisa possa fazer a condição do `while` mudar.

Exemplo:

```python
contador = 1

while contador <= 3:
    print(contador)
    contador = contador + 1
```

A linha:

```python
contador = contador + 1
```

faz o valor mudar a cada volta.

Quando:

```python
contador = 4
```

a condição:

```python
contador <= 3
```

resulta em:

```text
False
```

e o `while` termina.

---

# 4. Loop infinito

Se a condição nunca se tornar `False`, o programa pode entrar em um loop infinito.

Exemplo:

```python
contador = 1

while contador <= 3:
    print(contador)
```

O contador nunca muda.

Portanto:

```text
1 <= 3
```

será sempre:

```text
True
```

O programa continuará imprimindo `1`.

Regra importante:

> Todo `while` precisa ter uma forma de encerrar sua repetição.

Isso pode acontecer pela mudança da própria condição ou por comandos como `break`.

---

# 5. Ordem das instruções

O Python executa as linhas dentro do `while` na ordem em que foram escritas.

Exemplo:

```python
contador = 0

while contador < 5:
    contador = contador + 1
    print(contador)
```

Saída:

```text
1
2
3
4
5
```

Mesmo que a condição seja:

```python
contador < 5
```

o número `5` é exibido.

Isso acontece porque, quando o contador ainda vale `4`:

```text
4 < 5 → True
```

O Python entra na volta.

Depois:

```python
contador = contador + 1
```

transforma o valor em `5`.

E só então:

```python
print(contador)
```

exibe `5`.

A condição será verificada novamente somente no início da próxima volta.

---

# 6. Variáveis de controle

Um `while` não precisa necessariamente utilizar números.

Também podemos controlar a repetição através de outras variáveis.

Exemplo:

```python
continuar = "S"

while continuar == "S":
    print("Executando operação...")
    continuar = "N"

print("Programa encerrado.")
```

Quando `continuar` passa a valer `"N"`, a condição fica `False` e o `while` termina.

---

# 7. input()

A função `input()` permite receber informações digitadas pelo usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")
```

O programa:

1. exibe a mensagem;
2. aguarda o usuário digitar;
3. recebe o valor;
4. armazena o valor na variável.

Exemplo:

```python
nome = input("Digite seu nome: ")

print("Olá,", nome)
```

Se o usuário digitar:

```text
Maria
```

a variável passa a conter:

```python
nome = "Maria"
```

---

# 8. input() retorna str

Por padrão, o `input()` devolve uma `str`.

Se o usuário digitar:

```text
25
```

em:

```python
idade = input("Digite sua idade: ")
```

o valor armazenado será equivalente a:

```python
idade = "25"
```

e não:

```python
idade = 25
```

---

# 9. Conversão com int()

Quando queremos receber um número inteiro, podemos converter o resultado do `input()`:

```python
idade = int(input("Digite sua idade: "))
```

O fluxo é:

```text
Usuário digita 25
        ↓
input() devolve "25"
        ↓
int() converte "25"
        ↓
int() devolve 25
        ↓
idade recebe 25
```

Agora podemos realizar cálculos normalmente:

```python
nova_idade = idade + 5
```

---

# 10. Soma x concatenação

Quando usamos `+` com números:

```python
25 + 25
```

Resultado:

```text
50
```

Quando usamos `+` com strings:

```python
"25" + "25"
```

Resultado:

```text
2525
```

Neste caso não ocorre uma soma matemática.

As duas strings são concatenadas.

---

# 11. Operador diferente (!=)

O operador:

```python
!=
```

significa:

> diferente de

Exemplo:

```python
5 != 3
```

Resultado:

```text
True
```

Enquanto:

```python
5 != 5
```

Resultado:

```text
False
```

---

# 12. Sistema de login com while

Exemplo desenvolvido durante a sprint:

```python
senha_correta = 1234

senha_digitada = int(input("Digite sua senha: "))

while senha_digitada != senha_correta:
    print("Senha incorreta. Digite novamente")
    senha_digitada = int(input("Digite sua senha: "))

print("Login realizado")
```

Enquanto:

```python
senha_digitada != senha_correta
```

for `True`, o programa continua pedindo uma nova senha.

Quando o usuário digita `1234`:

```text
1234 != 1234 → False
```

o `while` termina.

---

# 13. break

O `break` encerra imediatamente uma estrutura de repetição.

Exemplo:

```python
contador = 1

while contador <= 10:
    print(contador)

    if contador == 3:
        break

    contador = contador + 1

print("Fim")
```

Saída:

```text
1
2
3
Fim
```

Mesmo que:

```python
contador <= 10
```

ainda seja `True`, o `break` força a saída do `while`.

Regra:

> `break` encerra o laço inteiro.

---

# 14. while True

Também podemos criar uma repetição propositalmente infinita:

```python
while True:
```

Nesse caso, precisamos de alguma forma de encerrá-la.

Um padrão comum é utilizar `break`.

```python
while True:
    senha = int(input("Digite sua senha: "))

    if senha == 1234:
        break

    print("Senha incorreta")

print("Login realizado")
```

O `while` continuaria para sempre, mas:

```python
break
```

permite encerrá-lo quando a condição desejada acontecer.

---

# 15. continue

O `continue` não encerra o laço inteiro.

Ele encerra apenas a volta atual e manda o Python começar a próxima.

Exemplo:

```python
contador = 0

while contador < 5:
    contador = contador + 1

    if contador == 3:
        continue

    print(contador)

print("Fim")
```

Saída:

```text
1
2
4
5
Fim
```

O número `3` não é exibido porque:

```python
if contador == 3:
    continue
```

faz o Python abandonar o restante daquela volta.

---

# 16. Diferença entre break e continue

## break

```python
break
```

Significa:

> Encerre o laço inteiro.

---

## continue

```python
continue
```

Significa:

> Encerre apenas esta volta e vá para a próxima.

Forma simples de lembrar:

```text
break    → acabou; saia do laço.
continue → pule esta volta; continue o laço.
```

---

# 17. break e continue juntos

Exemplo:

```python
while True:
    jogador = input("Digite o jogador: ")

    if jogador == "sair":
        break

    if jogador == "Neymar":
        continue

    print("Jogador cadastrado:", jogador)

print("Cadastro encerrado")
```

Neste programa:

- `"sair"` encerra completamente o cadastro;
- `"Neymar"` pula apenas aquela volta;
- qualquer outro jogador é cadastrado normalmente.

---

# 18. Desafio final - Acumulador de gols

Programa desenvolvido ao final da sprint:

```python
total_gols = 0

while True:
    gols = int(input("Digite o número de gols: "))

    if gols < 0:
        break

    total_gols = total_gols + gols

print("Total de gols:", total_gols)
```

Exemplo de entradas:

```text
1
2
3
-1
```

Acumulação:

```text
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
```

Quando o usuário digita:

```text
-1
```

o `break` acontece antes do acumulador.

Portanto, `-1` não entra na soma.

Resultado:

```text
Total de gols: 6
```

Observação:

```python
if gols < 0:
```

faz qualquer número negativo encerrar o programa.

Caso quiséssemos que somente `-1` encerrasse:

```python
if gols == -1:
    break
```

---

# Conceitos aprendidos

- `while`
- condição de repetição
- fluxo de execução do `while`
- loops infinitos
- variáveis de controle
- `input()`
- conversão de `str` para `int`
- concatenação de strings
- operador `!=`
- `while True`
- `break`
- `continue`
- diferença entre `break` e `continue`
- integração entre `while`, `if`, `input()` e acumuladores

---

# Anotações da Athena

Nesta sprint, os programas passaram a ser interativos.

Antes, os dados normalmente eram definidos diretamente no código:

```python
idade = 25
```

Agora o programa pode receber dados do usuário:

```python
idade = int(input("Digite sua idade: "))
```

Também foi aprendida uma diferença importante entre `for` e `while`.

O `for` é muito utilizado para percorrer elementos:

```python
for partida in partidas:
```

Já o `while` mantém uma repetição enquanto determinada condição for verdadeira:

```python
while senha_digitada != senha_correta:
```

Por fim, foram aprendidas duas formas de controlar uma repetição:

```text
break    → encerra o laço.
continue → pula a volta atual.
```

No desafio final, vários conhecimentos das sprints anteriores foram combinados:

```text
variável
   ↓
while
   ↓
input()
   ↓
int()
   ↓
if
   ↓
break
   ↓
acumulador
   ↓
resultado
```

Isso permitiu construir um programa que recebe uma quantidade indeterminada de dados do usuário, decide quando encerrar e acumula os valores informados.

## Regra principal da Sprint 11

> `while` repete enquanto uma condição for `True`.

E:

> Se nada puder tornar a condição `False` ou interromper o laço com `break`, podemos criar um loop infinito.