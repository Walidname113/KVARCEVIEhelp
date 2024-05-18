#!/usr/bin/env python

import subprocess
import time
import sys

try:
    from telethon.sync import TelegramClient
    from telethon.errors import SessionPasswordNeededError
    from telethon.tl.functions.messages import SendMessageRequest
    import asyncio
    import telethon
    import time
    import os
    import sys
    import aiohttp 
    import json
    from telethon import TelegramClient, events, utils
except ImportError:
    print("\033[0;31mНеобходимо установить недостающие библиотеки...\033[0m")
    time.sleep(3)
    subprocess.run(["clear"])
    subprocess.run(["bash", "configure.sh"])
    sys.exit()

def execute_code():
    print("\033[0;32mНужные библиотеки уже установленны. Запуск програмы...\033[0m")
    time.sleep(5)
    subprocess.run(["clear"])
    subprocess.run(["python3", "code.py"])

if all(hasattr(telethon, module) for module in ['sync', 'errors', 'tl']):
    execute_code()
