#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

libraries=("requests" "telebot" "aiogram" "asyncio" "telethon" "psutil" "Telegraph")

confirm_delete() {
    read -p "Вы действительно хотите удалить все установленные по умолчанию библиотеки? (Варианты ответа: да, нет, y, n, yes, no): " answer
    case "$answer" in
        [Yy]|[Yy][Ee][Ss]) return 0;;
        [Nn]|[Nn][Oo]) return 1;;
        *) echo "Некорректный ответ. Пожалуйста, введите 'да' или 'нет'.";;
    esac
}

uninstall_libraries() {
    if confirm_delete; then
        echo -e "${YELLOW}Удаление всех установленных по умолчанию библиотек...${NC}"
        for lib in "${libraries[@]}"; do
            pip uninstall -y "$lib" >/dev/null 2>&1
        done
        clear
        echo -e "${GREEN}Все установленные по умолчанию библиотеки успешно удалены.${NC}"
    else
        clear
        echo -e "${GREEN}Операция удаления отменена.${NC}"
    fi
}

uninstall_libraries
