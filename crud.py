#IMPORT DA FUNÇOES
from defs import *


while True:
    menu()

    try:

        escolha = int(input("Digite uma Opção: "))

    except ValueError:

        print("[red]Digite apenas números![/]")
        continue

    if escolha == 1:

        nome = str(input("Digite seu Nome: ")).strip()
        idade = ler_inteiro("Digite sua idade: ")
                
        sexo = ''
        while sexo not in ["M", "F"]:
            sexo = str(input("Digite seu sexo[F|M]: ")).strip().upper()
        numero = ler_inteiro("Digite seu número: ")
        criar_cadastro(nome, idade, sexo, numero)

    elif escolha == 2:
        
        lista_cadastro()

    elif escolha == 3:

        indice = ler_indice("Digite o indice para alterar: ")
        nome_novo = str(input("Novo nome:")).strip()
        idade_nova = ler_inteiro("Idade novo: ")
        sexo_novo = ''
        while sexo_novo not in ["M", "F"]:
            sexo_novo = input("Sexo novo: ").strip().upper()
        numero_novo = ler_inteiro("novo número: ")
        atualizar_cadastro(indice, nome_novo, idade_nova, sexo_novo, numero_novo)

    elif escolha == 4:

        indice = ler_indice("Qual indice deseja excluir: ")
        excluir_cadastro(indice)

    elif escolha == 5:

        print("Sistema Cadastro encerrado")
        break
    
    else:
        print("[red]Digite um Opção válida[/]")
    