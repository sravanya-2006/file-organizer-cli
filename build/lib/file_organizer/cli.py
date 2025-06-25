import sys
from pathlib import Path
import shutil
import logging

def main():
    logging.basicConfig(
        filename="organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )

    if len(sys.argv) < 2:
        print("Please provide a folder path.")
        sys.exit()

    folder = Path(sys.argv[1])

    if not folder.exists() or not folder.is_dir():
        print("That folder doesn't exist.")
        sys.exit()

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix[1:] or "no_extension"
            dest = folder / ext.upper()
            dest.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest / file.name))
            message = f"Moved: {file.name} → {dest}/"
            print(f"{message}")
            logging.info(message)
