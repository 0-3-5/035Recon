#!/bin/bash

current_directory=$(pwd)

echo "python3 \"${current_directory}/script/main.py\" \"\$@\"" > "${current_directory}/command/035Recon"

export PATH=$PATH:"${current_directory}/command"

echo 'export PATH=$PATH:"'${current_directory}'/command"' >> ~/.zshrc
echo 'export PATH=$PATH:"'${current_directory}'/command"' >> ~/.bashrc

chmod +x "${current_directory}/command/035Recon"

pip install selenium
pip install pillow
pip install colorama

source ~/.bashrc
source ~/.zshrc