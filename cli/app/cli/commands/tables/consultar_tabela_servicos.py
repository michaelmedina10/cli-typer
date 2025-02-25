import typer
from rich.console import Console
from cli.utils.mostrar_tabela import mostrar_tabela
from cli import variaveis_globais

import pandas as pd

app = typer.Typer()
console = Console()
tabela_carregada = None


@app.command(help="Retorna a tabela de servicos")
def servicos():
    df = pd.DataFrame(
        {
            "servico": [
                "servicoA",
                "servicoB",
                "servicoC",
            ],
            "situacao": [0, 0, 100],
        }
    )

    mostrar_tabela(df)
    variaveis_globais.tabela_global = df
