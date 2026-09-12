# Exercício 19 · Separando o nome

# Use split() para quebrar um nome completo em pedaços. Sem strtok, sem ponteiro, sem laço.

# Exercício 19

nome_completo = input("Digite seu nome completo: ")

partes = nome_completo.split()

print(partes)                 # o split devolveu o nome em partes
primeiro = partes[0]          # primeiro elemento de partes
ultimo = partes[-1]           # último elemento de partes

print(f"Primeiro nome: {primeiro}")         # mostre o último nome
print(f"Ultimo nome: {ultimo}")           # mostre o último nome
print(f"O nome tem {len(partes)} partes")   # quantas partes tem o nome