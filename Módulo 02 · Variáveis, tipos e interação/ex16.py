# Exercício 16 · Conversor de temperatura

# Leia uma temperatura em Celsius e converta para Fahrenheit: F = C * 9 / 5 + 32. Depois faça o caminho inverso em uma segunda parte, se quiser praticar.

# Exercício 16

celsius = float(input("Temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32       # formula

print(f"Essa temperatura em Fahrenheit é: {fahrenheit}")       # mostre algo como  25.0 C = 77.0 F