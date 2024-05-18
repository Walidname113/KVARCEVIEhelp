#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
cd && cd KRAVIENCEhelp && rm -rf install.sh update.sh code.py amain.py bootlibralies.sh configure.sh words.json > /dev/null 2>&1 || true && mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session ~/ > /dev/null 2>&1 || true
cd
rm -rf KRAVIENCEhelp > /dev/null 2>&1
pkg install git -y > /dev/null 2>&1
git clone https://github.com/Walidname113/KRAVIENCEhelp/ > /dev/null 2>&1
chmod -R 755 ~/KRAVIENCEhelp
cd
clear
mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session KRAVIENCEhelp > /dev/null 2>&1 || true
clear
cd
clear
cd KRAVIENCEhelp
if [ $? -eq 0 ]; then
    echo -e "$GREENОбновление прошло успешно!$NC"
    sleep 5
    clear
    bash install.sh
else
    echo -e "$REDОшибка при обновлении!$NC"
fi
