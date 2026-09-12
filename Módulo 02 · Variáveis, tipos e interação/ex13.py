# Exercício 13 · Falando com o usuário

# input() é o scanf do Python — sem & e sem %d. Peça o nome do usuário e cumprimente-o usando uma f-string.

# Exercício 13

nome = input("Digite seu nome: ")

print(f"Olá, {nome}")   # complete aqui: use {nome} dentro da f-string

# Cuidado: esquecer o f faz o programa imprimir literalmente {nome}
print("Olá, {nome}")   # rode e compare o resultado