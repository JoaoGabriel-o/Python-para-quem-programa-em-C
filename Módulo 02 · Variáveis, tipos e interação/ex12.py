# Exercício 12 · Convertendo tipos

# int() e float() fazem o papel de atoi() e atof(). str() dispensa o sprintf(). Lembre: a conversão devolve um valor novo, ela não altera a variável original.

# Exercício 12

texto_numero = "42"
texto_decimal = "3.14"
ano = 2026

n = 42       # complete aqui: converta texto_numero para int
d = 3.14     # complete aqui: converta texto_decimal para float
s = "2026"       # complete aqui: converta ano para str

print(n + 8)        # deve mostrar 50
print(d * 2)        # deve mostrar 6.28
print(s + "!")      # deve mostrar 2026!
print(type(n), type(d), type(s))