#13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
quilo = int(input("Digite o peso do alimento em quilos pls: "))
consumo: int = quilo * 1000 / 50
print(f"O alimento irá durar {consumo:.0f} dias")