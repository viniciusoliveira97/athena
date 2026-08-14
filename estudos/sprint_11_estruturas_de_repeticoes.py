senha_correta = False

while senha_correta == False:
    print("Senha incorreta. Tente novamente.")


contador = 1

while contador <= 3:
    print(contador)
    contador = contador + 1

print("Fim")


while contador <= 3:
    print(contador)
    contador = contador + 1


contador = 1

while contador <= 3:
    print(contador)

print("Fim")


senha_correta = False

while senha_correta == False:

    print("Digite a senha")

    senha_correta = True

print("Login realizado")


contador = 0

while contador < 5:
    contador = contador + 1
    print(contador)

print("Fim")


continuar = "S"

while continuar == "S":
    print("Executando operação...")
    continuar = "N"

print("Programa encerrado.")


nome = input("Digite seu nome: ")

print("Olá,", nome)


idade = input("Digite sua idade: ")

nova_idade = idade + idade

print(nova_idade)


numero = int(input("Digite um número: "))

resultado = numero + numero

print(resultado)


contador = 1

while contador <= 10:
    print(contador)

    if contador == 3:
        break

    contador = contador + 1

print("Fim")


while True:
    senha = int(input("Digite sua senha: "))

    if senha == 1234:
        break

    print("Senha incorreta")

print("Login realizado")


senha_correta = 1234

senha_digitada = int(input("Digite sua senha: "))

while senha_digitada != senha_correta:
    print("Senha incorreta. Digite novamente")
    senha_digitada = int(input("Digite sua senha: "))

print("Login realizado")


contador = 0

while contador < 5:
    contador = contador + 1

    if contador == 3:
        continue

    print(contador)

print("Fim")


while True:
    jogador = input("Digite o jogador: ")

    if jogador == "sair":
        break

    if jogador == "Neymar":
        continue

    print("Jogador cadastrado:", jogador)

print("Cadastro encerrado")


total_gols = 0

while True:
    gols = int(input("Digite o número de gols:"))

    if gols < 0:
        break

    total_gols = total_gols + gols


print("Total de gols:", total_gols)