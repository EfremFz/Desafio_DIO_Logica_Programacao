#Declarando a variavel nome do heroi
nome_heroi = input("Digite o nome do heroi: ")

#Declarando a variavel level do heroi
level_heroi = int(input("Digite o level do heroi: "))

#fazendo o loop para verificar o level do heroi e imprimir a mensagem correspondente

if level_heroi <= 1000:
    print("O herói " + nome_heroi + " está no nível de Ferro.")
elif 1001 <= level_heroi <= 2000:
    print("O herói " + nome_heroi + " está no nível de Bronze.")
elif 2001 <= level_heroi <= 5000:
    print("O herói " + nome_heroi + " está no nível de Prata.")
elif 5001 <= level_heroi <= 7000:
    print("O herói " + nome_heroi + " está no nível de Ouro.")
elif 7001 <= level_heroi <= 8000:
    print("O herói " + nome_heroi + " está no nível de Platina.")
elif 8001 <= level_heroi <= 9000:
    print("O herói " + nome_heroi + " está no nível de Acendente.")
elif 9001 <= level_heroi <= 10000:
    print("O herói " + nome_heroi + " está no nível de Imortal.")
else:
    print("O herói " + nome_heroi + " está no nível de Radiante.")
        