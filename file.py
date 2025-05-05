valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

# Calcular total do pedido
totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
precoFinal = totalHamburguer + totalBebida

# Calcular o troco
troco = valorPago - precoFinal

# Imprimir o resultado
print(f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}.")
