import requests
import time
import subprocess
import os

version_check_url = "https://raw.githubusercontent.com/Walidname113/KVARCEVIEhelp/main/version.txt"

def get_current_version():
    response = requests.get(version_check_url)
    if response.status_code == 200:
        return response.text.strip()
    return None

print("\033[1;33mПроверка на обновление...\033[0m")

def checkversion():
    current_version = get_current_version()
    expected_version = "1.2.4"
    
    if current_version and current_version != expected_version:
        time.sleep(3)
        print("\033[0;31mДоступно внешнее обновление. Обновляем...\033[0m")
        subprocess.run(["bash", "update.sh"])
    else:
        print("\033[0;32mОбновление не требуется. Проверяем наличие code.py...\033[0m")
        
        if os.path.isfile("code.py"):
            print("\033[0;32mЗапускаем юзербот...\033[0m")
            subprocess.run(["python3", "code.py"])
        else:
            print("\033[0;31mФайл code.py не найден. Запускаем установку...\033[0m")
            subprocess.run(["bash", "install.sh"])

checkversion()
