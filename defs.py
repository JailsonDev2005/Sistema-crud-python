#IMPORT RICH PERMITE EXIBIR TEXTO COLORIDO E FORMATADO NO TERMINAL
from rich import print
#CRIA TABELAS BONITAS E ORGANIZADAS
from rich.table import Table
#USADO PARA MOSTRA CONTEUDO DENTRO DE CAIXAS
from rich.panel import Panel


#GUARDA OS DADOS DO USUARIO
Dados = []


#MOSTRA O MENU DE OPÇÕES NO TERMINAL
def menu():

    conteudo = "Opções"
    conteudo += "\n1. Criar novo cadastro"
    conteudo += "\n2. Lista cadastro"
    conteudo += "\n3. Atualizar cadastro"
    conteudo += "\n4. Excluir cadastro"
    conteudo += "\n5. Sair"

    menu = Panel(conteudo,title="Sistema CRUD", width=28)

    print(menu)


#CRIA O CADASTRO DO USUARIO
def criar_cadastro(nome, idade, sexo, numero):

    cadastro = {"nome":nome, "idade":idade, "sexo":sexo, "numero":numero}
    Dados.append(cadastro)

    print("[bold green]Cadastro realizado com sucesso![/]")


#LISTA OS USUARIO
def lista_cadastro():

    if not Dados:
        print("[red]Nenhum cadastro encontrado[/]")
        return
    
    tabela = Table(title="Lista de Cadastros")

    tabela.add_column("ID", style="cyan", justify="center")
    tabela.add_column("Nome", style="green")
    tabela.add_column("Idade", style="yellow")
    tabela.add_column("Sexo", style="magenta")
    tabela.add_column("Número", style="blue")

    for indice, pessoas in enumerate(Dados):
        tabela.add_row(
            str(indice + 1),
            pessoas["nome"],
            str(pessoas["idade"]),
            pessoas["sexo"],
            str(pessoas["numero"])
        )

    print(tabela)


#EDITA OS CADASTROS DOS USUARIOS
def atualizar_cadastro(i, nome, idade, sexo, numero):

    if 0 <= i < len(Dados):
        Dados[i].update({
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "numero": numero
        })

        print("[green]Cadastro atualizado com sucesso![/]")

    else:

        print("[red]Atualização inválida[/]")


#EXCLUI OS CADASTROS DOS USUARIOS
def excluir_cadastro(i):

    if 0 <= i < len(Dados):
        cadastro_excluido = Dados.pop(i)
        print(f"[green]Cadastro {cadastro_excluido['nome']} removido com sucesso![/]")
    else:
        print("[red]Erro ao remover[/]")


#LER SE O NÚMERO E INTEIOR
def ler_inteiro(msg):

    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("[red]Digite apenas números[/]")

#LER O INDICE DIGITADO PELO USUARIO
def ler_indice(msg):

    while True:
        try:
            i = int(input(msg)) - 1
            if 0 <= i < len(Dados):
                return i
            print("[red]Índice fora da lista[/]")

        except ValueError:
            print("[red]Digite apenas números[/]")