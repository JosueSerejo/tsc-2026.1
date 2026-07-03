import random

peso1 = round(random.uniform(0, 1), 3)
peso2 = round(random.uniform(0, 1), 3)
peso3 = round(random.uniform(0, 1), 3)
peso_limiar = round(random.uniform(0, 1), 3)

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

soma_produtos = (valor1 * peso1) + (valor2 * peso2) + (valor3 * peso3) + (-1 * peso_limiar)

if soma_produtos >= 0:
    sinal_saida = 1
else:
    sinal_saida = -1

print("\nProcessamento do Perceptron")
print(f"Valores: [{valor1}, {valor2}, {valor3}]")
print(f"Pesos:   [{peso1}, {peso2}, {peso3}, {peso_limiar}]")
print(f"Peso do Limiar: {peso_limiar}")
print("-" * 40)
print(f"Potencial de Ativação:  {round(soma_produtos, 3)}")
print(f"Sinal de Saída Final:   {sinal_saida}")