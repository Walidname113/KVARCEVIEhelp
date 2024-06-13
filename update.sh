#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
cd
pkg install git > /dev/null 2>&1
cd KVARCEVIEhelp

# Проверяем, существует ли старый файл Codecrypt.py, и удаляем его, если да
if [ -f Codecrypt.py ]; then
    rm Codecrypt.py
fi

# Выполняем обновление репозитория и устанавливаем новый файл Codecrypt.py
git fetch origin > /dev/null 2>&1
git reset --hard origin/main > /dev/null 2>&1
clear
echo -e "$GREENОбновление прошло успешно.$NC"
bash install.sh
