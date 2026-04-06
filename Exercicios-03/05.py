num_1 = (int(input("Qual o primeiro número?")))
num_2 = (int(input("Qual o segundo número?")))
print(num_1 % num_2)
if num_1 % num_2 == 0:
    print("São múltiplos!")
else:
    print("Não são múltiplos")