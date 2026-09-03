#5. Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais).
import math
nA = int(input("Digite o valor de A: "))
nB = int(input("Digite o valor de B: "))
nC = int(input("Digite o valor de C: "))

delta: float = nB ** 2 - 4 * nA * nC
bask1: float = (-nB + math.sqrt(delta)) / (2 * nA)
bask2: float = (-nB - math.sqrt(delta)) / (2 * nA)
print(f"As raízes reais são: {bask1} e {bask2}")