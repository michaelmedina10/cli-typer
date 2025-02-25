import typer

app = typer.Typer()


@app.command(help="Finaliza o serviço")
def sair():
    raise typer.Abort()
