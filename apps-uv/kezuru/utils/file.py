from pathlib import Path

from utils.type_guard import isNull


def get_file_state_time(path: Path) -> float:
    return path.stat().st_mtime


def get_path_of_latest_file(folder: str) -> str | None:
    """
    Return the path to the latest *.html file in the `folder` directory (by mtime).
    If none exist, return `None`.

    Args:
        folder: Path to folder to search for .html files.
    """
    folder_path = Path(folder)
    html_files: list[Path] = list(folder_path.glob("*.html"))

    if isNull(html_files):
        return None

    latest: Path = max(html_files, key=get_file_state_time)

    return str(latest)


def create_directrory(dir: str | Path) -> None:
    dir_path = Path(dir)
    dir_path.mkdir(parents=True, exist_ok=True)


def save_text_to_file(dir: Path, filename: str, contents: str) -> None:
    create_directrory(dir)

    with open(
        dir / filename,
        mode="w",
        encoding="utf-8",
    ) as file:
        file.write(contents)


def debug_save_text_to_file(
    contents: str, file_name: str = "temp.html", dir: Path = Path("./temp/")
) -> None:
    save_text_to_file(dir=dir, filename=file_name, contents=contents)
