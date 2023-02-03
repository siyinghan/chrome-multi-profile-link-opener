"""
Run scripts to open a link with different Chrome profiles at once.
"""
import logging
import sys
from os import path
from pathlib import Path
from subprocess import call
from sys import argv
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    profiles = ["Profile 2", "Profile 3", "Profile 4", "Profile 5"]
    path = path.join(Path(__file__).parent.absolute(), "open_chrome.sh")
    for profile in profiles:
        call([path, profile, argv[1]])
        logging.info(f"Open ({profile}): {argv[1]}")
        sleep(1)
    logging.info("Done!")
