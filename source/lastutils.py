import typer
from typing_extensions import Annotated
from module.spotlight import get_spotlight

app = typer.Typer(help="Ultimate Windows Utilities v1.0")


@app.command()
def spotlight(
        path: Annotated[str, typer.Option(show_default="current folder", help="Set output path", )] = "",
        ext: Annotated[str, typer.Option(help="Set image extension")] = "png",
        prefix: Annotated[str, typer.Option(help="Set prefix for filename")] = "",
        smartphone: Annotated[bool, typer.Option(help="Include vertical images for smartphone")] = False,
):
    """
    Get Lockscreen Spotlight Wallpaper
    """
    return_code = get_spotlight(ext, path, prefix, smartphone)

    if return_code != 0:
        raise typer.Abort()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
