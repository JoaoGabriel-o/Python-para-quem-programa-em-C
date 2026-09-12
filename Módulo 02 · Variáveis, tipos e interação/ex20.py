# Exercício 20 · Ficha de cadastro · fechamento

# Fechamento do módulo: reúne entrada, conversão, cálculo, split(), upper() e f-string em um único programa.

# Exercício 20 · fechamento do Módulo 2

nome_completo = input("Nome completo: ")   # leia a nome com string
idade = int(input("Idade: "))              # leia a idade como int
altura = float(input("Altura: "))          # leia a altura como float
n1 = float(input("Nota 1: "))              # leia nota 1 como float
n2 = float(input("Nota 2: "))              # leia nota 2 como float

notas = [n1, n2]
soma_valores = sum(notas)          # sum(notas): soma todos os elementos da lista (parte de cima da fração da média)
total_itens = len(notas)           # len(notas): conta a quantidade total de itens que estão dentro da lista (divisor / denominador)

partes = nome_completo.split()
primeiro = partes[0]                   # primeiro nome
media = soma_valores / total_itens     # Divide a soma total dos valores pela quantidade de itens para obter a média aritmética

print()
print("===== FICHA DE CADASTRO =====")
print(f"Nome: {nome_completo.upper()}")
print(f"Primeiro nome: {primeiro}")           # Tratamento: primeiro nome
print(f"Ano de nascimento: {2026 - idade}")   # Idade e ano de nascimento aproximado (2026 - idade)
print(f"Altura: {altura:.2f}")                # Altura com 2 casas decimais
print(f"Média: {media:.2f}")                  # Média com 1 casa decimal
print("=============================")