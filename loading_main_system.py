from rich.console import Console
from time import sleep


def loading_main_question():
    console = Console()
    with console.status("[bold green]Chargement des données...", spinner='material', spinner_style='green') as status:
        sleep(5)