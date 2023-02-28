# open-link-in-multi-profiles

Open the Chrome folder to check Chrome profiles.

```zsh
$ open ~/Library/Application\ Support/Google/Chrome
```

## Getting Started

### Executable File

#### Create the executable file

```zsh
$ pyinstaller --onefile --noconsole --noupx --icon=icon.ico --add-data 'open_chrome.sh:.' --name OpenChromeProfiles gui.py
```

```zsh
$ pyinstaller OpenChromeProfiles.spec
```

#### Debug

```zsh
$ ./dist/OpenChromeProfiles --debug=all
```

### Command-Line Tool

#### Add an alias

```zsh
$ echo '\nalias open-chrome="python ~/Documents/GitHub/open-link-in-multi-profiles/main.py"' >> ~/.zshrc
```

```zsh
$ source ~/.zshrc
```

## Usage

### Open one link in Chrome profiles

To open one link in Chrome profiles, run the following command:

```zsh
$ open-chrome <link>
```

Replace <link> with the actual link you want to open.

### Open multiple links in Chrome profiles

To open multiple links in Chrome profiles, follow these steps:

1. Create a new shell script file with the following command:
   ```zsh
   $ touch open-chrome.sh
   ```
2. Open the file with a text editor and add the following lines:
   ```zsh
   #!/bin/zsh
   
   alias open-chrome="python /path/to/open-link-in-multi-profiles/main.py"
   
   # open link1
   open-chrome <link1>
   # open link2
   open-chrome <link2>
   # open link3
   open-chrome <link3>
   ```
   Replace /path/to/ with the actual path to the repository folder, and <link1>, <link2>, and <link3> with the actual
   links you want to open.
3. Save and close the file.
4. Run the script with the following command:
   ```zsh
   $ sh open-chrome.sh
   ```