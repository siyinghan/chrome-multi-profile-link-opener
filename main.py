"""
Open a specified link in Google Chrome using different profiles from the command line.
"""
from pathlib import Path
from sys import argv

from open_chrome import open_chrome

if __name__ == "__main__":
    sh_path = Path(__file__).resolve().parent
    open_chrome(sh_path, argv[1])
