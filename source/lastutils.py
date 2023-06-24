import typer
import sub_rename
from typing_extensions import Annotated
from module.spotlight import get_spotlight
from module.checksum import run_checksum
from module.grep import grep

app = typer.Typer(help="LastUtils v1.0")
app.add_typer(sub_rename.app, name="rename")


@app.command()
def grep(
        path: Annotated[str, typer.Argument(help="Search path", show_default=False)],
        text: Annotated[str, typer.Argument(help="Search text", show_default=False)],
):
    """
    Find text in Excel
    """
    return_code = grep(path, text)

    if return_code != 0:
        raise typer.Abort()


@app.command()
def checksum(
        path: Annotated[str, typer.Argument(help="Path of folder or file to process")],
        algo: Annotated[str, typer.Option(
            help="\bSpecify process algorithms. Separated by comma (,)\r\n"
                 "\bAvailable algorithms:\r\n"
                 "md5, sha256, sha512, sha3-256, sha3-512, blake2b, blake2s")] = "all",
):
    """
    Generate and verify files hashes
    """
    return_code = run_checksum(path, algo)

    if return_code != 0:
        raise typer.Abort()


@app.command()
def spotlight(
        path: Annotated[str, typer.Option(show_default="current folder", help="Set output path", )] = "",
        ext: Annotated[str, typer.Option(help="Set image extension")] = "jpg",
        prefix: Annotated[str, typer.Option(help="Set prefix for filename")] = "",
        phone: Annotated[bool, typer.Option(help="Include vertical images for smartphone")] = False,
):
    """
    Get Lockscreen Spotlight Wallpaper
    """
    return_code = get_spotlight(ext, path, prefix, phone)

    if return_code != 0:
        raise typer.Abort()


@app.command()
def update():
    """
    Check for new release
    """
    print(f"Checking...")


@app.command()
def info():
    """
    Show application information
    """
    print(f"Hello")


if __name__ == "__main__":
    app()
