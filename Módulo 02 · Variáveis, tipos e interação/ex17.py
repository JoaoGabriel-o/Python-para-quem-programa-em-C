# Exercício 17 · Explorando uma string

# Strings em Python não são vetores de char terminados em \0 — elas trazem ferramentas prontas.

# Python	            Equivalente em C
# len(s)	            strlen(s)
# a + b	                strcat(a, b)
# a == b	            strcmp(a, b) == 0
# s.upper() / s.lower()	laço com toupper()
# s.strip()	            laço manual
# s.split()	            strtok(...)

# Exercício 17

frase = "   Python é legal   "

print(len(frase))
print(frase.upper())          # frase em maiúsculas
print(frase.lower())          # frase em minúsculas
print(frase.strip())          # frase sem os espaços das pontas
print(len(frase.strip()))     # quantos caracteres tem a frase SEM os espaços das pontas

# Concatenação e comparação
a = "casa"
b = "Casa"
print(a + b)
print(a == b)   # a é igual a b?