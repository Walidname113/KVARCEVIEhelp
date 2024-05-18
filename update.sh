#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'

echo -e "$YELLOWПодождите пожалуйста, выполняется обновление...$NC"
cd || { echo -e "$REDНе удалось перейти в домашний каталог!$NC"; exit 1; }
cd KRAVIENCEhelp || { echo -e "$REDНе удалось перейти в каталог KRAVIENCEhelp!$NC"; exit 1; }
rm -rf install.sh update.sh code.py amain.py bootlibralies.sh configure.sh words.json > /dev/null 2>&1 || { echo -e "$REDОшибка удаления файлов!$NC"; }
mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session ~/ > /dev/null 2>&1 || { echo -e "$REDОшибка перемещения файлов!$NC"; }
cd || { echo -e "$REDНе удалось перейти в домашний каталог!$NC"; exit 1; }
rm -rf KRAVIENCEhelp > /dev/null 2>&1 || { echo -e "$REDОшибка удаления каталога KRAVIENCEhelp!$NC"; }
pkg install git -y > /dev/null 2>&1 || { echo -e "$REDОшибка установки git!$NC"; exit 1; }
git clone https://github.com/Walidname113/KRAVIENCEhelp/ > /dev/null 2>&1 || { echo -e "$REDОшибка клонирования репозитория!$NC"; exit 1; }
chmod -R 755 ~/KRAVIENCEhelp || { echo -e "$REDОшибка изменения прав доступа!$NC"; exit 1; }
cd || { echo -e "$REDНе удалось перейти в домашний каталог!$NC"; exit 1; }
mv command_prefix.txt chat_ids.txt interval.txt sessioncash.txt send_status.txt ocrestrinatedub.session KRAVIENCEhelp > /dev/null 2>&1 || { echo -e "$REDОшибка перемещения файлов обратно!$NC"; }
cd KRAVIENCEhelp || { echo -e "$REDНе удалось перейти в каталог KRAVIENCEhelp!$NC"; exit 1; }

if [ $? -eq 0 ]; then
    echo -e "$YELLOWОбновление прошло успешно, но для полного применения обновлений, введите следующую команду: ` cd && cd KRAVIENCEhelp && bash install.sh ` эта команда перезагрузит необходимые данные. Извините, пока что это не поддерживается автоматически!$NC"
else
    echo -e "$REDОшибка при обновлении!$NC"
fi
