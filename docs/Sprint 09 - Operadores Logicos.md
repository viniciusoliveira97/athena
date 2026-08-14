# Sprint 09 - Operadores Lógicos

## Objetivo

Aprender a combinar condições utilizando os operadores lógicos `and`, `or` e `not`.

Esses operadores permitem criar decisões mais completas e são utilizados em praticamente todos os programas.

---

## Operador `and`

O operador `and` significa **"e"**.

Para que o resultado seja `True`, **todas** as condições devem ser verdadeiras.

### Estrutura

```python
if condicao1 and condicao2:
    print("As duas condições são verdadeiras.")
```

### Exemplos

```python
True and True
```

Resultado:

```python
True
```

```python
True and False
```

Resultado:

```python
False
```

### Tabela

| Condição 1 | Condição 2 | Resultado |
|------------|------------|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## Operador `or`

O operador `or` significa **"ou"**.

Para que o resultado seja `True`, basta que **uma** das condições seja verdadeira.

### Estrutura

```python
if condicao1 or condicao2:
    print("Pelo menos uma condição é verdadeira.")
```

### Exemplos

```python
True or False
```

Resultado:

```python
True
```

```python
False or False
```

Resultado:

```python
False
```

### Tabela

| Condição 1 | Condição 2 | Resultado |
|------------|------------|-----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Operador `not`

O operador `not` significa **"não"**.

Ele inverte um valor booleano.

### Exemplos

```python
not True
```

Resultado:

```python
False
```

```python
not False
```

Resultado:

```python
True
```

### Tabela

| Valor original | Resultado |
|----------------|-----------|
| True | False |
| False | True |

---

## Combinando operadores

É possível utilizar vários operadores na mesma condição.

Exemplo:

```python
venceu = True
fez_tres_gols = False

if venceu and not fez_tres_gols:
    print("O time venceu, mas não marcou três gols.")
```

Para resolver condições maiores, é recomendado analisar uma parte de cada vez.

Exemplo:

```python
not venceu or fez_tres_gols
```

Passos:

1. Resolver o `not`.
2. Substituir pelo resultado.
3. Resolver o `and` ou `or`.

Esse método facilita a leitura e evita erros.

---

## Quando utilizar

Utilize operadores lógicos quando for necessário combinar duas ou mais condições.

Exemplos:

- Login de usuários.
- Controle de permissões.
- Validação de dados.
- Jogos.
- Sistemas de cadastro.
- Análise de partidas de futebol.

---

## Erros comuns

- Confundir `and` com `or`.
- Esquecer que `not` inverte o valor booleano.
- Tentar resolver uma condição grande de uma única vez.
- Esquecer que o `and` exige que todas as condições sejam verdadeiras.

---

## Resumo

- `and` → Todas as condições devem ser verdadeiras.
- `or` → Basta uma condição ser verdadeira.
- `not` → Inverte um valor booleano.
- Condições complexas devem ser resolvidas passo a passo.

---

# Anotações da Athena

Nesta sprint foi introduzido o conceito de operadores lógicos.

O objetivo não foi apenas decorar tabelas de verdadeiro e falso, mas compreender o raciocínio por trás de cada operador.

Também foi desenvolvido um método para analisar condições complexas:

1. Resolver primeiro o `not`.
2. Substituir o resultado.
3. Resolver o `and` ou `or`.

Esse processo será utilizado durante todo o restante da jornada, especialmente quando começarmos a trabalhar com funções, filtros de dados, pandas e Machine Learning.