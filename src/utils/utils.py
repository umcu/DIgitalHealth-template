import logging
import os
from pathlib import Path


def create_directory(filepath: str) -> None:
    """Create parent directory."""
    path = Path(filepath)
    if not os.path.exists(path.parent):
        logging.info(f"Creating directory {path.parent}")
        os.makedirs(path)
