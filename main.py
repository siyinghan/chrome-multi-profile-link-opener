"""
Run scripts to open a link with different Chrome profiles at once.
"""
import logging
import sys
from pathlib import Path
from subprocess import call
from sys import argv
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def open_chrome(link):
    """
    Opens a URL in Google Chrome for multiple profiles.

    Parameters:
        link (str): The URL to open in Google Chrome.

    Returns:
        None

    Raises:
        OSError: If the `open_chrome.sh` script cannot be found.

    Example:
        >>> link = "https://www.example.com"
        >>> open_chrome(link)
        Opens the URL "https://www.example.com" in Google Chrome for multiple profiles.

    """
    # profiles = ["Profile 2", "Profile 3", "Profile 4", "Profile 5", "Profile 7", "Profile 8", "Profile 9",
    #             "Profile 10", "Profile 11"]
    profiles = ["Profile 2", "Profile 3"]
    path = Path(__file__).resolve().parent / "open_chrome.sh"

    # Check if the script exists before attempting to call it
    if not path.exists():
        raise OSError("open_chrome.sh script not found")

    for profile in profiles:
        call([str(path), profile, link])
        logging.info(f"Opened ({profile}): {link}")
        sleep(1)

    logging.info("All profiles opened successfully!")


if __name__ == "__main__":
    open_chrome(argv[1])
