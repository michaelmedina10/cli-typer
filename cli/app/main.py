import typer
from rich.console import Console
from cli.commands.common import limpar_tela, interromper
from cli.commands.tables import consultar_tabela_servicos, filtrar
from cli.commands import (
    carregar_historico,
    salvar_historico,
)
from cli.utils.interfaces.menu import menu

app = typer.Typer()
console = Console()

app.add_typer(limpar_tela.app)
app.add_typer(interromper.app)
app.add_typer(consultar_tabela_servicos.app)
app.add_typer(filtrar.app)


def main():
    menu()
    carregar_historico()
    while True:
        try:
            command = input("\nprojeto > ").strip().split()
            if not command:
                continue
            app(command)
        except SystemExit as e:
            if e.code == 1:
                raise e
            elif e.code == 2:
                typer.echo("Comando inválido, digite --help para verificar os comandos")
        except (KeyboardInterrupt, EOFError):
            salvar_historico()


if __name__ == "__main__":
    main()
