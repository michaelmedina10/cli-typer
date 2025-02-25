import sys

# Importa a biblioteca correta dependendo do sistema operacional
if sys.platform == "win32":
    import pyreadline3 as readline
else:
    import readline  # Linux/macOS já têm readline embutido

HISTORY_FILE = ".command_history"


def carregar_historico():
    try:
        readline.read_history_file(HISTORY_FILE)
    except FileNotFoundError:
        pass


def salvar_historico():
    readline.write_history_file(HISTORY_FILE)


def adicionar_ao_historico(command: str):
    readline.add_history(command)
