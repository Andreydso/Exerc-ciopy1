#16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

horasdejob = float(input("Digite a quantidade de horas trabalhadas: "))
valorhorajob = float(input("Digite o valor por hora: "))
furto = float(input("Digite o percentual de desconto (em %): "))
filhote = int(input("Digite o número de dependentes: "))

salbruto: float = horasdejob * valorhorajob
furto2: float = salbruto * (furto / 100)
salliquido: float = salbruto - furto2
salareceber: float = salliquido + (filhote * 100)

print(f"O salário a receber é: R${salareceber:.2f}")
