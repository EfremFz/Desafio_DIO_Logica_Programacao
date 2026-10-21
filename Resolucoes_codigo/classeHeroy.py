import json
from pathlib import Path


# Variável para armazenar o caminho do arquivo JSON
arquivo = Path(__file__).parent / "date" / "ataques.json"


# Carregar os dados dos ataques do arquivo JSON
with open(arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


# Criando a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo, ataque):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ataque = ataque

# Criação da classe Ataque
class Ataque(Heroi):
    def __init__(self,nome, idade, tipo, ataque):
        super().__init__(nome, idade, tipo, ataque)

    def exibir_ataques(self):
        print(f"O {self.tipo} atacou com {self.ataque}!")


# Criando a lista de opções com quebras de linha (\n)
menu = """
=== Escolha a Classe ===
[1] MAGO
[2] GUERREIRO
[3] MONGE
[4] NINJA
======================
Escolha o numero correspondente à classe: """

# Exibindo o menu

print("================================")
print("    Fixa de dados do Heroi      ")
print("================================")
nome = input("Digite o nome do Heroi: ")
idade = int(input("Digite a idade do Heroi: "))

# Imprimindo o menu e solicitando a escolha do tipo de herói
print(menu)
tipo = input()


# Utilizando o match-case para determinar o tipo de herói com base na escolha do usuário
match tipo:
    case "1":
        tipo = "MAGO"
    case "2":
        tipo = "GUERREIRO"
    case "3":
        tipo = "MONGE"
    case "4":
        tipo = "NINJA"
    case _:
        print("Opção inválida!")
        exit()


# Usando um FOR para varrer o json e estrair os ataques correspondentes ao tipo de herói escolhido
for classe, descricao in dados["classes_ataque"].items():
    if classe == tipo.lower():
        ataque = descricao
        break

# Criando o objeto heroi para ser usado pela classe Ataque e exibindo os ataques do herói
heroi = Ataque(nome, idade, tipo, ataque)

# Exibindo os ataques do herói
heroi.exibir_ataques()
