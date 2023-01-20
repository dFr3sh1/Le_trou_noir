from rich.console import Console
from time import sleep


def loading_game():
        console = Console()

        with console.status("[bold green]Initialisation...") as status:
                sleep(7)