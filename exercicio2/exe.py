#2. Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.
sala = float(input("Digite o salário do funcionário: "))
aumento: float= sala * 0.15
novosala: float = sala + aumento
print(f"O novo salário com reajuste de 15% é: R${novosala}")