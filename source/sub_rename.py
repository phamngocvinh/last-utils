import typer
from typing_extensions import Annotated
from module import rename

app = typer.Typer(help="Rename multiple files")


@app.command()
def replace(
        path: Annotated[str, typer.Argument(help="Path of folder to process")],
        from_text: Annotated[str, typer.Argument(help="String to find")],
        to_text: Annotated[str, typer.Argument(help="String to replace")]):
    """
    Replace text
    """
    rename.replace(path, from_text, to_text)
    return 0
