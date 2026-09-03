#7. Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
com = int(input("Digite o valor do comprimento do paralelepípedo: "))
lar = int(input("Digite o valor do largura do paralelepípedo: "))
alt = int(input("Digite o valor do altura do paralelepípedo: "))

volume: int = com * lar * alt
print(f"O volume do paralelepípedo será de: {volume}cm³")
