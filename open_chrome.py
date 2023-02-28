"""
Run scripts to open a link with different Chrome profiles at once.
"""
import logging
import sys

from pathlib import Path
from subprocess import call
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def open_chrome(sh_path: Path, link: str) -> None:
    """
    Opens a URL in Google Chrome with different profiles.

    Parameters:
        sh_path (Path): Path to the directory containing the `open_chrome.sh` script.
        link (str): The URL to open in Google Chrome.

    Raises:
        OSError: If the `open_chrome.sh` script cannot be found.

    Returns:
        None

    Example:
        >>> link = "https://www.example.com"
        >>> sh_path = Path("/path/to/directory")
        >>> open_chrome(sh_path, link)
        Opens the URL "https://www.example.com" in Google Chrome with different profiles.

    """
    # Profiles to open
    profiles = ["Profile 2", "Profile 3", "Profile 4", "Profile 5", "Profile 7", "Profile 8", "Profile 9",
                "Profile 10", "Profile 11"]

    # Path to the `open_chrome.sh` script
    path = sh_path / "open_chrome.sh"

    # Check if the script exists before attempting to call it
    if not path.exists():
        raise OSError("open_chrome.sh script not found")

    # Set permissions on `open_chrome.sh` if necessary
    if not path.stat().st_mode & 0o100:
        path.chmod(0o755)

    try:
        for profile in profiles:
            call([str(path), profile, link])
            logging.info(f"Opened ({profile}): {link}")
            sleep(1)
        logging.info("All profiles opened successfully!")
    except OSError as e:
        logging.error(f"Error opening link: {e}")
