nota_1 = (float(input("Digite sua primeira nota")))
nota_2 = (float(input("Digite sua segunda nota")))
nota_3 = (float(input("Digite sua terceira nota")))
nota_4 = (float(input("Digite sua quarta nota")))
nota_total = (nota_1 + nota_2 + nota_3 + nota_4)
nota_final = (nota_total / 4)
print(nota_final)
if nota_final >= 7:
    print('Aprovado!')
elif 5 <= nota_final <= 6:
    print("Recuperação!")
elif nota_final < 5:
    print("Reprovado!")
else:
    print('Erro!')