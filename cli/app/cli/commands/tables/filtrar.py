from cli import variaveis_globais
from cli.utils.mostrar_tabela import mostrar_tabela
import typer

app = typer.Typer()


@app.command(help="Filtrar tabela passando coluna e valor")
def filtrar(
    coluna: str = typer.Option("", "--coluna", help="Nome da coluna da tabela"),
    valor: str = typer.Option("", "--valor", help="Valor a ser buscado na tabela"),
):
    tipo_coluna = variaveis_globais.tabela_global[coluna].dtype.name

    conversores = {
        "int64": int,
        "float64": float,
        "object": str,
        "bool": lambda x: x.lower() in ["true", "1", "t"],
    }
    conversor = conversores.get(tipo_coluna, "str")
    novo_valor = conversor(valor)

    mostrar_tabela(
        variaveis_globais.tabela_global[
            variaveis_globais.tabela_global[coluna] == novo_valor
        ]
    )
