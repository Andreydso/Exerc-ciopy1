#17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
temp = float(input("Digite a duração do percurso em horas: "))
velo = float(input("Digite a velocidade média do veiculo em kilometros: "))

dist: float = temp * velo
litro: float = dist / 12
print(f"A quantidade de litros gastos foi: {litro:.2f} L")