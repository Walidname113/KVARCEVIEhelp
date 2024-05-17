#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

clear

echo -e "$YELLOWУстановка Userbot'a. Подождите пожалуйста.$NC"

pkg install openssl-tool > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo -e "${RED}Ошибка при установке openssl-tool.${NC}"
  exit 1
fi

pkg install python3 -y > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo -e "${RED}Ошибка при установке python3.${NC}"
  exit 1
fi

# Расшифровка файла
openssl aes-256-cbc -d -salt -pbkdf2 -in codecrypt.py -out code.py -k "Ocrestrinated"
if [ $? -eq 0 ]; then
  echo -e "$GREENЮзербот успешно установлен. Запуск юзербота...$NC"
  python3 amain.py
else
  echo -e "${RED}Ошибка CODE 4.${NC}"
fi
