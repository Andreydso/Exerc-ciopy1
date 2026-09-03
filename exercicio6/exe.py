#6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
x, y = y, x
print(f"Os valores de X e Y trocados são: X = {x} e Y = {y}")