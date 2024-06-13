#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
cd
pkg install git > /dev/null 2>&1
cd KVARCEVIEhelp

random_suffix=$(date +%s | sha256sum | base64 | head -c 8)
old_filename="Codecrypt_old_${random_suffix}.py"

if [ -f Codecrypt.py ]; then
    mv Codecrypt.py $old_filename
fi

git fetch origin > /dev/null 2>&1
git reset --hard origin/main > /dev/null 2>&1
clear
echo -e "$GREENОбновление прошло успешно.$NC"

# Удаляем старый файл с случайным именем
if [ -f $old_filename ]; then
    rm $old_filename
fi

bash install.sh
