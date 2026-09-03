#15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
cat1 = float(input("Digite o valor do primeiro cateto: "))
cat2 = float(input("Digite o valor do segundo cateto: "))
hipo: float = (cat1**2 + cat2**2) ** (1/2)
print(f"O valor da hipotenusa é: {hipo:.2f}")
