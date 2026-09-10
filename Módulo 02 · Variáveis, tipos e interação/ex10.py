# Exercício 10 · Descobrindo o tipo

# Use `type()` para descobrir o tipo de cada variável do exercício anterior.

idade = 18        # complete aqui: tipo de idade
altura = 1.73     # complete aqui: tipo de altura
nome = 'Gabriel'  # complete aqui: tipo de nome
aprovado = True   # complete aqui: tipo de aprovado

print(type(idade))
print(type(altura))
print(type(nome))
print(type(aprovado))

# E este aqui? Por que o resultado é str, e não int?
# Porque o valor "20" está entre aspas, então o Python interpreta como texto (str).
print(type("20"))