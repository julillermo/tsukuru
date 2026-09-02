import os
import shutil
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from rich import print as rprint

load_dotenv()


def main():
    db_url = os.getenv("DB_URL")

    # ===== Generate JLPT data =====
    rprint("[green]🥄 Running JLPT scraping and data generation ... [/green]")
    jlpt_data_dir = Path("./data/")  # Relative to project root
    if jlpt_data_dir.exists() and any(
        path.is_file() and path.name != ".gitkeep" for path in jlpt_data_dir.iterdir()
    ):
        rprint(
            "[yellow]JLPT Data already generated; skipping repeat of JLPT data generation.[/yellow].\n"
        )
    else:
        generate_jlpt_data = subprocess.run(
            [
                "uv",
                "run",
                "./apps-uv/kezuru/main.py",
                "--output-dir",
                "./data/",
                "-ds",
                "1",
                "-ic",
            ],
            cwd="./",
            text=True,
            check=False,
        )
        if generate_jlpt_data.returncode != 0:
            raise RuntimeError(
                f"Importer go binary failed with exit code {generate_jlpt_data.returncode}:\n{generate_jlpt_data.stderr}"
            )
        rprint(f"[green]Go DB import[/green]:\n{generate_jlpt_data.stdout}")

    # ===== Apply DB migrations =====
    rprint("[green]🧳 Running database migrations ...[/green]")
    goose = shutil.which("goose")
    if goose is None:
        raise RuntimeError("Could not find goose on Path.")

    goose_result = subprocess.run(
        [
            goose,
            "-dir",
            "./apps-go/jisho/sql/migrations/",
            "postgres",
            f"{db_url}",
            "up",
        ],
        cwd="./",
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )

    if goose_result.returncode != 0:
        raise RuntimeError(
            f"Goose failed with exit code {goose_result.returncode}:\n{goose_result.stderr}"
        )
    rprint(f"[green]goose[/green]: {goose_result.stderr}")

    # ===== Import Data into DB =====
    rprint("[green]📤️ Running import to DB logic ... [/green]")
    db_import_success_marker_path = Path("/var/lib/tsukuru/import-complete")

    if (
        db_import_success_marker_path.exists()
        and db_import_success_marker_path.is_file()
    ):
        rprint(
            "[yellow]DB import already completed; skipping redundant DB import step.[/yellow]"
        )
    else:
        db_import_result = subprocess.run(
            [
                "./apps-go/jisho/bin/exec/importer/app",
            ],
            cwd="./",
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
        if db_import_result.returncode != 0:
            raise RuntimeError(
                f"Importer go binary failed with exit code {db_import_result.returncode}:\n{db_import_result.stderr}"
            )
        rprint(f"[green]Go DB import[/green]:\n{db_import_result.stdout}")

        db_import_success_marker_path.touch(exist_ok=True)

        rprint("[green]👍️ DB import completed.[/green]")

    print("Finished `run_self-host` script")


if __name__ == "__main__":
    main()
