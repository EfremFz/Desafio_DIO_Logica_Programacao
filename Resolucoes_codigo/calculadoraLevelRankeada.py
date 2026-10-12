#Declaração das váriaveis
nomeJogador = input("Informe o nome do jogador: ")
qtdVitorias = int(input("Informe a quantidade de vitórias do jogador: "))
qtdDerrotas = int(input("Informe a quantidade de derrotas do jogador: "))

#Função para calcular o level do jogador

def calcularLevel(qtdVitorias, qtdDerrotas):
    
    rank = (qtdVitorias) - (qtdDerrotas)
    return rank

#Criando a variavel saldo para receber o retorno da função calcularLevel
saldo = calcularLevel(qtdVitorias, qtdDerrotas)


#Fazendo o loop para verificar o level do jogador

if saldo <= 10:
    nivel = "FERRO"
elif 11 <= saldo <= 20:
    nivel = "BRONZE"
elif 21 <= saldo <= 50:
    nivel = "PRATA"
elif 51 <= saldo <= 80:
    nivel = "OURO"
elif 81 <= saldo <= 90:
    nivel = "DIAMANTE"
elif 91 <= saldo <= 100:
    nivel = "LENDRÁRIO"
else:
    nivel = "IMORTAL"


#Imprimindo o resultado final

print(
    f"O jogador {nomeJogador} está no nível {nivel}, "
    f"com saldo de vitórias de {saldo}."
)

#O f antes da string permite concatenar as váriaveis diretamente na string, sem precisar usar o operador +.