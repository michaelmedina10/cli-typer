from rich.console import Console

console = Console()


def menu():
    console.print("------------------------------------------------------------")
    console.print("Menu Principal:", style="bold blue")
    console.print("------------------------------------------------------------")
    console.print("|limpar              |   limpar a tela")
    console.print("|sair                |   sair do programa")
    console.print("|servicos   |   carregar tabela controle servicos")
    console.print("-----------------------------------------------------------\n")
