#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
pkg install git
cd KRAVIENCEhelp
git pull
clear
echo -e "$GREENОбновление прошло успешно.$NC"
bash configure.sh
