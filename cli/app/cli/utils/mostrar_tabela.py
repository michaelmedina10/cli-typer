from rich.table import Table
from rich.console import Console
import pandas as pd


console = Console()


def mostrar_tabela(df: pd.DataFrame):
    table = Table(show_header=True, header_style="bold magenta")
    for col in df.columns:
        table.add_column(col, justify="right")

    for _, row in df.iterrows():
        table.add_row(*[str(val) for val in row])

    console.print(table)
