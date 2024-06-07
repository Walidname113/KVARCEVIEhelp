#!/usr/bin/env python

import subprocess
import time
import sys

try:
    import asyncio
    import telethon
    import os
    import requests 
    import json
    import psutil
except ImportError:
    print("\033[0;31mНеобходимо установить недостающие библиотеки...\033[0m")
    time.sleep(3)
    subprocess.run(["clear"])
    subprocess.run(["bash", "configure.sh"])
    sys.exit()

def execute_code():
    print("\033[0;32mНужные библиотеки уже установлены. Запуск...\033[0m")
    time.sleep(5)
    subprocess.run(["clear"])
    subprocess.run(["python3", "code.py"])

execute_code()
