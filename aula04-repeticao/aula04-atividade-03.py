qtd_musicas = int(input("Digite a quantidade de músicas que você tem na playlist (DB): "))
num_musicas = int(input("Digite o numero das músicas da sua playlist: "))

for i in range (0, qtd_musicas):
    for j in range (0, num_musicas):
        print(f" i: {i}, j:{j}")