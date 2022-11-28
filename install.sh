#!/usr/bin/env bash

tempFolder="$HOME/.pets-cli"
appUrl="https://github.com/arielsrv/pets-cli"

if [ -d "$tempFolder" ]; then
  rm -rf "$tempFolder"
else
  mkdir -p "$tempFolder"
fi

git clone "$appUrl" "$tempFolder"
python3 -m pip install --upgrade pip setuptools wheel
pip install -U pyinstaller
(
  cd "$tempFolder" || exit
  pyinstaller pets/main.py
)

echo "$tempFolder/dist/pets/pets"
FILE="/usr/local/bin/pets"
if [ ! -L "$FILE" ]; then
  sudo ln -s "$tempFolder/dist/pets/pets" /usr/local/bin/pets
fi

#eval "$(_PETS_COMPLETE=bash_source pets)"
#eval "$(_PETS_COMPLETE=zsh_source pets)"
