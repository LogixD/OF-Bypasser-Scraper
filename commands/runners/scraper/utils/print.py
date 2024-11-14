import utils.console as console
from __version__ import __version__


def print_start():
    console.get_shared_console().print(
        f"[bold green]Version {__version__}[/bold green]"
    )
