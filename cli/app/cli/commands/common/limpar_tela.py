import typer

app = typer.Typer()


@app.command(help="Limpar a tela de terminal do usuário")
def limpar():
    typer.echo("\033[H\033[J", nl=False)
