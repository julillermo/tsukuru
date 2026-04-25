from pathlib import Path


def get_file_state_time(path: Path) -> float:
    return path.stat().st_mtime


def get_path_of_latest_file(folder: str) -> str | None:
    """
    Return the path to the latest *.html file in `folder` (by mtime). If none exist, return None.

    Args:
        folder: Path to folder to search for .html files.
    """
    folder_path = Path(folder)

    html_files: list[Path] = list(folder_path.glob("*.html"))
    if not html_files or len(html_files) < 1:
        return None

    latest: Path = max(html_files, key=get_file_state_time)
    return str(latest)
