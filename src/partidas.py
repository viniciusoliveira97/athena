import csv

with open("data/campeonato-brasileiro-full.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    partidas = list(leitor)