# Sprint 10 - Funções (`def`)

## Objetivo

Aprender a criar funções para organizar o código, reutilizar instruções e devolver resultados utilizando `return`.

---

## O que é uma função?

Uma função é um bloco de código responsável por executar uma tarefa específica.

Ela permite escrever um conjunto de instruções apenas uma vez e reutilizá-lo sempre que necessário.

Exemplo:

```python
def cumprimentar():
    print("Olá!")
```

Definir uma função **não significa executá-la**.

---

## Chamando uma função

Para executar uma função, basta escrever seu nome seguido de parênteses.

```python
cumprimentar()
```

Saída:

```
Olá!
```

Uma mesma função pode ser chamada quantas vezes forem necessárias.

```python
cumprimentar()
cumprimentar()
cumprimentar()
```

---

## Blocos de código

Assim como acontece com `if` e `for`, tudo o que estiver identado após o `def` pertence à função.

```python
def cumprimentar():
    print("Olá!")
    print("Bem-vindo ao Athena!")
    print("Bom estudo!")
```

Toda a identação representa as instruções da função.

---

## Parâmetros

Uma função pode receber informações.

Essas informações são chamadas de parâmetros.

```python
def cumprimentar(nome):
    print("Olá,", nome)
```

Neste exemplo:

- `nome` é um parâmetro.

---

## Argumentos

Quando chamamos uma função, enviamos um valor.

Esse valor é chamado de argumento.

```python
cumprimentar("Carlos")
```

Neste exemplo:

- parâmetro → `nome`
- argumento → `"Carlos"`

---

## Variáveis x Parâmetros

A função recebe valores, e não o nome das variáveis.

Os três exemplos abaixo produzem exatamente o mesmo resultado.

```python
cumprimentar("Carlos")
```

```python
pessoa = "Carlos"

cumprimentar(pessoa)
```

```python
usuario = "Carlos"

cumprimentar(usuario)
```

Em todos os casos, o parâmetro `nome` recebe o valor `"Carlos"`.

---

## Contextos diferentes

Uma variável criada fora da função não é a mesma variável do parâmetro.

```python
def cumprimentar(nome):
    print(nome)

pessoa = "Carlos"

cumprimentar(pessoa)

print(pessoa)
```

Saída:

```
Carlos
Carlos
```

O parâmetro existe apenas durante a execução da função.

A variável continua existindo normalmente após a função terminar.

---

# Return

O `return` serve para devolver um valor ao local onde a função foi chamada.

Exemplo:

```python
def somar(a, b):
    return a + b
```

Quando fazemos:

```python
resultado = somar(10, 20)
```

O Python executa:

```
10 + 20 = 30
```

Depois devolve o valor `30`.

Então:

```python
resultado = 30
```

---

## Diferença entre print e return

### print()

Mostra uma informação na tela.

```python
def somar(a, b):
    print(a + b)
```

O valor aparece na tela, mas não pode ser reutilizado.

---

### return

Devolve um valor para o restante do programa.

```python
def somar(a, b):
    return a + b
```

Agora o resultado pode ser armazenado em uma variável.

```python
resultado = somar(10, 20)
```

Ou utilizado em novos cálculos.

```python
dobro = somar(10, 20) * 2
```

---

## Fluxo de execução

```python
def somar(a, b):
    return a + b

x = somar(10, 5)

y = x * 2

print(y)
```

Ordem de execução:

1. A função é definida.
2. A função é chamada.
3. Os parâmetros recebem os valores.
4. A função calcula `a + b`.
5. O `return` devolve `15`.
6. `x` recebe `15`.
7. `y` recebe `30`.
8. O `print` exibe `30`.

---

## Conceitos aprendidos

- O que é uma função.
- Como definir uma função (`def`).
- Como chamar uma função.
- Blocos de código.
- Parâmetros.
- Argumentos.
- Diferença entre variáveis e parâmetros.
- Diferença entre `print` e `return`.
- Como utilizar o valor devolvido por uma função.

---

# Anotações da Athena

Nesta sprint foi apresentado um dos conceitos mais importantes da programação: funções.

Foi aprendido que funções organizam o código, evitam repetições e permitem reutilizar lógica.

Também foi introduzido o `return`, responsável por devolver um resultado ao restante do programa.

A principal conclusão da sprint é:

- `print()` mostra um valor.
- `return` devolve um valor.

Essa diferença será utilizada em praticamente todos os projetos futuros, especialmente quando começarmos a trabalhar com módulos, arquivos, pandas e análise de dados.