#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
cd && cd KRAVIENCEhelp && mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session amain.py bootlibralies.sh configure.sh LICENSE README.md words.json install.sh ~/ > /dev/null 2>&1 || true
rm -rf KRAVIENCEhelp > /dev/null 2>&1
pkg install git -y > /dev/null 2>&1
git clone https://github.com/Walidname113/KRAVIENCEhelp/ > /dev/null 2>&1
cd
clear
mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session amain.py bootlibralies.sh configure.sh LICENSE README.md words.json install.sh KRAVIENCEhelp > /dev/null 2>&1 || true
clear

if [ $? -eq 0 ]; then
    echo -e "$GREENОбновление прошло успешно!$NC"
    sleep 5
    clear
    python3 amain.py
else
    echo -e "$REDОшибка при обновлении!$NC"
fi
