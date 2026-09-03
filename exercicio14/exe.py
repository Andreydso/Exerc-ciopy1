#14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3o ângulo.
ang1 = int(input("Digite o primeiro ângulo do triângulo: "))
ang2 = int(input("Digite o segundo ângulo do triângulo: "))
ang3 = 180 - (ang1 + ang2)
print(f"O valor do terceiro ângulo é: {ang3}°")
