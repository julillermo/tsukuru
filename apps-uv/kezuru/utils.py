from pathlib import Path

__all__ = ["get_path_of_latest_file"]


def get_path_of_latest_file(folder: str) -> str | None:
    """
    Return the path to the latest *.html file in `folder` (by mtime).
        If none exist, return None.

    Args:
        folder: Path to folder to search for .html files.
    """
    folder_path = Path(folder)

    html_files = list(folder_path.glob("*.html"))
    if not html_files or len(html_files) < 1:
        return None

    latest = max(html_files, key=lambda p: p.stat().st_mtime)
    return str(latest)
