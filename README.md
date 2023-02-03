# open-link-in-multi-profiles

Open the Chrome folder to check Chrome profiles.

```zsh
$ open ~/Library/Application\ Support/Google/Chrome
```

## Preparation

```zsh
$ echo '\nalias open-chrome="python ~/Documents/GitHub/open-link-in-multi-profiles/main.py"' >> ~/.zshrc
```

```zsh
$ source ~/.zshrc
```

## Quickstart

### Open one link in Chrome profiles

```zsh
$ open-chrome https://www.google.com/
```

### Open multi-links in Chrome profiles

```zsh
$ touch open-chrome.sh
```

Copy to the new created `open-chrome.sh` and replace the links.

```shell
#!/bin/zsh

alias open-chrome="python ~/Documents/GitHub/python-run-shell-script/open_chrome.py"

# open link1
open-chrome https://www.google.com/
# open link2
open-chrome https://www.google.com/
# open link3
open-chrome https://www.google.com/
```

```zsh
$ sh open-chrome.sh
```