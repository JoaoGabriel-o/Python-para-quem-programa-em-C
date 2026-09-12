# Exercício 15 · Média de duas notas

# Leia duas notas, calcule a média e mostre o resultado com duas casas decimais usando f"{media:.2f}".

# Exercício 15

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

notas = [n1, n2]                   # Junta as notas recebidas dentro de uma lista chamada 'notas'
soma_valores = sum(notas)          # sum(notas): soma todos os elementos da lista (parte de cima da fração da média)
total_itens = len(notas)           # len(notas): conta a quantidade total de itens que estão dentro da lista (divisor / denominador)

media = soma_valores / total_itens # Divide a soma total dos valores pela quantidade de itens para obter a média aritmética

# Exibe o resultado formatado:
# - f"" permite interpolar variáveis dentro da string usando chaves {}
# - :.2f formata o valor numérico para exibir exatamente 2 casas decimais
print(f"Média: {media:.2f}")