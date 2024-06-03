from datetime import datetime, timedelta
import json
import asyncio
import os
import random
import telethon
from telethon import TelegramClient, events, utils, Button
import time
import sys
import requests
import subprocess
from telethon.tl.types import MessageEntityMention
import platform
import psutil
from telethon.tl.custom import Button
from telegraph import Telegraph
import tempfile
from io import BytesIO

telegraph = Telegraph()
telegraph.create_account(short_name='test')

subprocess.run(["clear"])

print("\033[0;32mЮзербот успешно запущен!\033[0m")

start_time = datetime.now()

shablon = ["ⳡⲉ ⳅⲁ ⲃыⲉⳝⲟⲏы ⲡⲟⲱⲗυ Ⲣⲉⲕⲥ ⲉⳝⲁⲏыύ ⲧы ⳡⲉ ⳅⲁⳝыⲗ ⲕⲧⲟ ⲧⲃⲟύ ⲡⲣⲁⲣⲟⲇυⲧⲉⲗь υ ⳡьⲉύ ⲧы ⲥⲡⲉⲣⲙⲟύ яⲃⲗяⲉⲱьⲥя ⲏⲩ ⲏⲉ ⳝⲟύⲥя я ⲧⲉ ⲭⲩⲉⲙ ⲙⲟⳅⲅυ ⲟⳝⲣⲁⲧⲏⲟ ⲃⲥⲧⲁⲃⲗю","ⲡⲟⲉⳝⲉⲙ ⲃ ⲡⲣυⲏцυⲡⲉ ⳝⲗяⲇⲥⲕⲟⲅⲟ ⲥⲃυⲏⲁ ⲧⲁⲕⲟⲅⲟ ⲡⲣⲟⲥⲧⲟ ⲏⲉ ⲇⲁύ ⳡⲁⲥⲩ ⲧⲉⲗⲕⲁ ⲉⲁⲏⲁя ⲁⲣя","ⲧы ⲏⲉ ⲇⲟⲥⲧⲟυⲏ ⲇⲁⲯⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲡⲟύⲙυ ⲥⲃυⲉⲟⲡⲟⲧⲁⲙ ⲧы ⲉⳝⲁⲏыц ⲡⲟⲉⳝⲉⲙ ⲧⲉⳝя ⲧⲩⲧ ⲃ ⲣⲟⲧⲁⲏ ⲧⲃⲟύ ⲥⲙⲉⲣⲇяⳃυύ","я ⲯⲉ ⲃⲉⲥь ⲧⲃⲟύ ⲅⲟⲃⲏⲟⲣⲟⲇ ⲃыⲉⳝⲩ ⲏⲉⲡⲟⲥⲣⲉⲇⲥⲧⲃⲉⲏⲏⲟ ⲕⲁⲕυⲙ ⲧⲟ ⲏⲁⲭⲩύ ⲟⲅⲩⲣцⲟⲙ ⲥыⲏⲩⲗя ⲱⲁⲃⲕυ ⲉⳝⲁⲏыύ ⲥⲟⲥυ ⲙⲏⲉ","ⲧы ⲯⲉ ⲯⲉⲣⲧⲃⲁ υⳅⲏⲟⲥυⲗⲟⲃⲁⲏυя ⲕⲁⳝⲁⳡⲕⲟⲙ я ⲧⲃⲟю ⲧⲩⲱⲕⲩ ⲥⲏυⲙⲩ ⲥ ⲧⲉⳝя υ ⲡⲟⲃⲉⲱⲩ ⲡⲭⲩⲉⲃⲱυц ⲏⲁⲣυⲕ ⲧⲩⲡⲟ ⲧⲟⲣⳡⲟⲕ я ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲕⲩⲃⲁⲗⲇⲟύ ⳝⲩⲇⲩ ⲡⲟ ⲅⲟⲗⲟⲃⲉ ⲡυⳅⲇυⲧь я ⳡⲉⲣⲉⲡ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲁⲗьцⲁⲙυ ⲣⲁⳅⲇⲁⲃⲗю ⲁ ⳅⲩⳝы ⲧⲃⲟⲉύ ⲯυⲣⲏⲟύ ⲙⲁⲧⲩⲭυ ⲃⲉⲥⲟⲙ 190ⲕⲅ ⲃыⳝью ⲭⲩⲉⲙ υ цыⲅⲁⲏⲥⲕυⲉ ⲅⲏυⲗыⲉ ⲙⲟⳅⲅυ ⲧⲃⲟⲉύ ⳝⲁⳝⲩⲱⲕυ ⲥⲟⲧⲣⲩ ⲃ ⲡⲣⲁⲭ","ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲇыⲣⲕⲁ ⲃ ⲕⲟⲧⲟⲣⲩю я ⲥⲩю ⲥⲃⲟύ ⲭⲩύ ⲩ ⲧⲉⳝя ⳝⲁⲧⲉⲕ ⲩⲯⲉ ⲟⲧ ⲙⲟυⲭ υⳅⳝυⲉⲏυύ ⲕⲟⲗяⲥⲟⳡⲏυⲕ ⲥυⲇυⲧ ⲣыⲇⲁⲉⲧ я ⲡⲣⲟⲥⲧⲟ ⲃⲥю ⲧⲃⲟю ⲣⲟⲇⲟⲥⲗⲟⲃⲏⲩю ⲉⲃⲣⲉύⲥⲕⲟύ ⲃⲏⲉⲱⲏⲟⲥⲧυ ⲥⲟⲯⲅⲩ ⲃ ⲥⲕⲩⲏⲥⲕⲁⲙⲉⲣⲉ ⲯⲁⲗⲕⲟⲉ ⲡⲟⲇⲟⳝυⲉ ⳡⲉⲗⲟⲃⲉⲕⲁ ⲧы ⲧⲩⲡⲟ ⲣⲟⲇυⲏⲕⲁ ⲏⲁ ⲗυцⲉ ⲥⲧⲁⲣⲟύ ⳝⲁⳝⲕυ ⲗыⲥыύ ⲡυⲇⲟⲣ я ⲧⲉⳝя ⲥⲃⲟⲉύ ⲙⲟⳡⲟύ ⲟⳝⲗⲩⳡυⲗ ⲁ ⲏⲁⲡⲟⲣⲟⲙ ⲥⲃⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ ⲣⲁⳅⲣⲩⳝυⲗ ⲧⲃⲟⲉ ⲯⲗⲕⲟⲉ ⲧⲉⲗьцⲉ ⲏⲁ 2 ⳡⲁⲥⲧυ","я ⲥⲃⲟυⲙυ ⲅⲁⲃⲏⲁⲇⲁⲃⲃⲙυ ⲡⲣⲟⲭⲟⲯⲃⲥь ⲡⲟ ⲧⲃⲟⲉⲙⲩ ⲗυцⲩ ⲟⳝⲟⲇⲣⲁⲏⲏыύ ⲇⲟ ⲏυⲧⲟⲕ ⲟⳝⲣⲩⳝⲟⲕ ⲥⲁⲗⲁ ⲭⲟⲧя ⲧы ⲇⲁⲯⲉ ⲏⲉ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲥυⲗⲟύ ⲙыⲥⲗυ ⳅⲁⲡⲣⲁⲅⲣⲟⲙυⲣⲟⲃⲁⲗ ⲏⲁ ⲥⲟⲥⲁⲏυⲉ ⳡⲗⲉⲏⲁ ⲏⲟ ⲧы ⲣⲁⳝⲟⲧⲁⲉⲱь ⲥⲟ ⲥⳝⲟяⲙυ υ ⲥⲟⲥⲉⲱь ⲏⲉ ⲧⲟⲗьⲕⲟ ⲭⲩύ ⲥⲟύ ⲏⲟ υ ⲃⲥⲉ ⲭⲩύυ ⲃ ⲣⲁⲇυⲩⲥⲉ 300 ⲙⲉⲧⲣⲟⲃ ⲩ ⲙⲉⲏя ⲯⲉ ⲕⲟⲏⳡⲁ ⲕⲁⲕ ⲕυⲥⲗⲟⲧⲁ ⲡⲟэⲧⲟⲙⲩ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⲥⲧⲟⲗьⲕⲟ ⲇыⲣⲟⲕ ⲡⲣⲟⲥⲧⲟ ⳝⲗяⲇⲥⲕⲁя ⲱⲗюⲭⲁ ⲥⲟⳝυⲣⲁюⳃяя ⲏⲁ ⲗⲉⳡⲉⲏυⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ","я ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⳝⲩⲇⲩ ⲡυⳅⲇυⲧь эⲧⲩ ⲱⲗюⲭⲉⲏцυю ⲃ ⲏⲉⲉ цⲉⲗыύ ⳝⲁⲣⲇⲉⲗь ⲭⲩⲉⲃ ⲃⲟύⲇⲉⲧ я ⲉⲉ ⲡⲣⲟⲥⲧⲟ ⳅⲁⲧⲣⲁⲭⲃю ⲇⲟ ⲡⲟⲧⲉⲣυ ⲡⲩⲗьⲥⲁ ⲁ ⲩ ⲧⲉⳝя ⲃⲟ ⲃⲣⲉⲙя ⲡⲣⲟⲥⲙⲟⲧⲣⲁ ⳝⲩⲇⲉⲧ υⲇⲧυ ⲕⲣⲟⲃь υⳅ ⲏⲟⲥⲁ υ ⲣⲩⲕⲁ ⲟⲏυⲙⲉⲉⲧ ⲟⲧ ⲇⲉⲣⲯⲁⲏυя ⲭⲩя ⲩ ⲥⲉⳝя ⲃ ⲯⲟⲡⲉ, я ⲡⲣяⲙ ⳃⲁⲥ ⲙⲟⲅⲩ ⲧⲃⲟυⲙυ ⳅⲩⳝⲁⲙυ ⲟⲧⳝυⲧь ⲭⲩύ ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲁ ⲇⲟ ⲡⲟⲥυⲏⲉⲏυⲉ ⲁ ⲧⲃⲟю ⲡⲣⲁⳝⲁⳝⲩⲱⲕⲩ ⲃⲟ ⲃⲣⲉⲙя ⲃⲧⲟⲣⲟύ ⲣыⳝⲟύ ⲟⲧⲡⲣⲁⲃυⲗ ⲏⲁ ⲧⲟⲧ ⲥⲃⲉⲧ υ ⲥⲕⲟⲣⲙυⲗ ⲙⲉⲥⲧⲏыⲙ ⲇⲉⲧяⲙ ⲧы ⲡⲟⲗⲩⲇⲟⲭⲗыύ ⲥⲃυⲏⲧⲩⲥ ⲭⲩⲇⲟύ ⲅⲟⲏⲇⲟⲏ ⲧⲩⲡⲟ ⲕⲟⲥⲧυ ⳝⲗяⲇь","ⲧⲩⲡⲟ ⲉⳝⲁⲱυⲣⲟⲃⲁⲗ ⲉⲉ ⲡⲟ ⳡⲉⲗюⲥⲧυ ⲕⲁⲕ ⲕυⲏⲅⲩⲣⲩ ⲏⲁ ⲏⲉύ ⳝⲟⲕⲥυⲣⲟⲃⲁⲗ ⲏьюⲫⲁⲅ ⳝⲗяⲇⲥⲕυύ я ⲟⲧⲡⲩⳃⲩ ⲣⲩⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⳝⲩⲇⲉⲧ ⲥⲟ ⲥⲕⲟⲗы ⲡⲁⲇⲁⲧь я ⲯⲉ ⳝⲗяⲇь ⲗⲉⲅⲕⲟ ⲙⲟⲅⲩ ⲧⲃⲟю ⲇⲩⲱⲩ ⲡⲣυⲟⳝⲣⲉⲥⲧυ я ⲯⲉ ⳅⲩяⳡю ⲧⲉⳝя ⲡⲟ ⳝⲟⲱⲕⲉ ⲏυⳃⲉⲏⲥⲕⲁя ⲕⲁⳝⲁⲏυⲭⲁ ⲡⲟⳡⲁⲡⲁⲗⲁ ⲅⲩⳝⲟύ ⲡⲁⲇⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲟⲧⲟⲣыύ ⲗюⳝыⲙυ ⲥⲡⲟⲥⲟⳝⲁⲙυ ⲡыⲧⲁⲉⲧⲥя ⲟⲧⲃⲉⲣⲅⲁⲧь ⲥⲗюⲏⲩ ⲥ ⲧⲃⲟⲉύ ⲅⲩⳝы ⲅⲏυⲗⲟⳅⲩⳝыύ ⲟⳝⲥⲟⲥ","ⲏⲉ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲥυⲗⲟύ ⲙыⲥⲗυ ⳅⲁⲡⲣⲁⲅⲣⲟⲙυⲣⲟⲃⲁⲗ ⲏⲁ ⲥⲟⲥⲁⲏυⲉ ⳡⲗⲉⲏⲁ ⲏⲟ ⲧы ⲣⲁⳝⲟⲧⲁⲉⲱь ⲥⲟ ⲥⳝⲟяⲙυ υ ⲥⲟⲥⲉⲱь ⲏⲉ ⲧⲟⲗьⲕⲟ ⲭⲩύ ⲥⲟύ ⲏⲟ υ ⲃⲥⲉ ⲭⲩύυ ⲃ ⲣⲁⲇυⲩⲥⲉ 300 ⲙⲉⲧⲣⲟⲃ ⲩ ⲙⲉⲏя ⲯⲉ ⲕⲟⲏⳡⲁ ⲕⲁⲕ ⲕυⲥⲗⲟⲧⲁ ⲡⲟэⲧⲟⲙⲩ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⲥⲧⲟⲗьⲕⲟ ⲇыⲣⲟⲕ ⲡⲣⲟⲥⲧⲟ ⳝⲗяⲇⲥⲕⲁя ⲱⲗюⲭⲁ ⲥⲟⳝυⲣⲁюⳃяя ⲏⲁ ⲗⲉⳡⲉⲏυⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟ 100 ⲣⲩⳝⲗⲉύ ⲡⲟⲕⲁ ⲩ ⲧⲉⳝя ⲟⲧⲉц ⲏⲁ ⲇυⲃⲁⲏⲉ ⲥ ⳝⲩⲧыⲗⲕⲟύ ⲡυⲃⲟ ⲥⲙⲟⲧⲣяⳃυύ ⲧⲉⲗⲉⲃυⳅⲟⲣ ⲏⲁ ⲥⲃⲟⲉύ υⲏⲃⲁⲗυⲇⲏⲟύ ⲕⲟⲗяⲥⲕⲉ ⳝⲉⲥⲡⲟⲙⲟⳃⲏⲟ ⲡⲣⲟⲥυⲧ ⲡⲣυⲏⲉⲥⲧυ  ⲯυⲣⲏⲩю ⲯⲟⲡⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ","ⲧы ⲉⳝⲁⲏⲏⲁя ⳡⲟ ⲙⲏⲉ ⲭⲩⲉⲕ ⲥⲟⲥⲉⲱь ⲧⲁⲕ ⲡⲗⲟⲭⲟ ⲏⲩ-ⲕⲁ ⲃⳅяⲗ ⲙⲟύ ⲭⲩύ υ ⲏⲁⳡⲁⲗ ⲟⲧⳝⲉⲗυⲃⲁⲧь ⲉё ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲏⲩ я ⲃⲉⲇь ⲧⲉⳝя ⲇⲩⲣⲩ ⲧⲩⲧ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟ ⲥⲁⲙыⲉ ⲅⲗⲁⲏⲇы ⲡⲟⲕⲁ ⲧы ⲏⲁ ⲟⲧⲕυⲏⲉⲱ ⲕⲟⲏⲉύ ⳝⲗяⲇυⲏⲁ ⲧы ⲏⲉⲏⲁⲥыⲧⲏⲁя ⲏⲩ я ⲃⲉⲇь ⲧⲉⳝⲉ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲩⲧ ⲥⲟⲧⲣяⲥⲉⲏυⲉ ⲙⲟⳅⲅⲁ ⲩⲥⲧⲣⲟю ⲏⲩ ⳝⲩⲇⲩ ⲕⲁⲯⲇⲩю ⲕⲟⲥⲧь ⲧⲃⲟυⲭ ⲣёⳝⲉⲣ ⲗⲟⲙⲁⲧь ⲡⲟⲕⲁ ⲧы ⲏⲁ ⲥⲧⲁⲏυⲱ ⲏⲉⲙⲟⳃⲏыⲙ ⲩⲉⳝⲁⲏⲁⲙ ⲏⲩ ⲧы ⳡⲟ ⲡⲟⲃⲉⲣυⲗ ⲃ ⲥⲉⳝя υⲗυ ⳡⲟ я ⲃⲟⲧ ⲏⲉ ⲡⲟύⲙⲩ ⲧы ⳡⲟ ⲇⲟ ⲥυⲭ ⲡⲟⲣ ⳅⲁⲡⲟⲙⲏυⲧь ⲏⲉ ⲙⲟⲯⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲧы ⲃυⲇυⲱь ⲙⲉⲏя ⲧы ⲇⲟⲗⲯⲉⲏ ⲡⲣⲟⲥⲧⲟ ⳅⲁⲕⲣыⲧь ⲥⲃⲟⲉ ⲯⲁⲗⲕⲟⲉ ⲉⳝⲁⲗⲟ","ⲇⲁ ⲙⲏⲉ ⲃⲟⲟⳝⳃⲉ ⲡⲟⲭⲩύ ⲧы ⲡⲟⲉⲱь υⲗυ ⲏⲟⲉ ⲇⲁⲃⲁύ ⲣⲉⲱⲉ ⲡυⲱυ ⲥⲃⲟⲙυ ⲧюⲗⲡⲁⲱⲕⲁⲙυ ⲏⲁⳅц ⲏⲁ ⲙⲟⲃⲉⲡ ⲡⲕ ⳅⲁ ⲡяⲧь ⲕⲟⲡⲉⲉⲕ υ ⲃⲥⲉ ⳡⲧⲟ ⲯⲉ. ⲃⲧ ⲙⲟⲅ ⲥⳅⲕⲁⲧьⲥⳡ ⲕ ⲙⲟⲉⲙⲩ ⳝⲟⲗьⲱυⲙⲩ ⲭⲩю ⲏⲁⳅцⲧⲯⲉ ⲧы ⲥⲃυⲏⲕⲁ ⳝⲟⲗⲇυⲏⲥⲕⲁя ⲧы ⲏⲉ ⲃⳅⲇⲩⲙⲁύ ⲙⲏⲉ ⲡⲣⲟⲥⲧⲁⲃь ⲏⲁ ⳡⲁⲥ ⲕⲁⲕ ⲧⲃⲟύ ⲉⳝⲗυⲃыύ ⲡⲟⲇⲣⲩⲅⲁ ⲕⲧⲣⲟⲅⲟⲧⲩⲯⲉ ⲏⲁⲭⲩύ ⲃⲥⲉ яύцⲁ ⲡⲣⲉⲣⲉⳅⲗⲁ ⳡⲧⲟыⳝⲧⳝⲟⲗьⲱⲉⲧⲧⲟⲕⲟⲅⲟ ⲏⲉ ⲥⲗыⲱⲁⲗ ⲟⲧ ⲧⲉⳝя ⲏⲁⲭⲩύ ⲥⲃυⲏⲕⲁ ⲇⲁⲃⲁύ ⲣⲉⲱⲉ ⲡυⲱυ ⲙⲏⲉ ⲡⲟ Ⲕⲗⲁⲃⲉ ⲡⲟⲕⲁ ⲧⲃⲟю ⲯυⲣⲏⲩю ⲧⲩⲱⲩ ⲙⲁⲙⲕⲩ ⲧⲁⲕ ⲥυⲗьⲏⲟ υⳅⳝυⲃⲁю ⲃⲥⲉⲙ ⳡⲁⲧⲟⲙ ⲕⲁⲕ ⲟⲏⲁ ⲡⲟⲧⲙⲟ ⲥυⲇυⲧ υ ⲏⲟⲉⲧ ⳡⲧⲟ ⲉύ ⲧⲁⲕ ⲥυⲗьⲏⲟ ⳝⲟⲗьⲏⲟ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲯⲉ ⲧы ⲏⲉ ⲇⲟⲏⲟⲥⲟⲕ ⲉⳝⲗυⲃыύ ⲃⲣⲟⲇⲉ ⲧⲉⳝя ⲏⲉ ⲭⲩя ⲣⲉⲃυ ⲏⲉ υⲇⲉⲧ ⲧⲉⳝⲉ ⲃ ⲉⳝⲗⲟ ⲥⲣⲁⳅⲩ ⲗⲉⲧυⲧ ⳝⲟⲗьⲱⲉ ⲟⲇⲏⲟⲅⲟ ⲙυⲗⲗυⲟⲏⲁ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы","ⲡⲟⲧⲉⲱⲏⲁя ⲧⲉⲗⲕⲁ ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⳝⲩⲇⲉⲧ ⲧяⲅⲁⲧьⲥя ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲧⲩⲧ ⳝⲩⲇⲉⲧ ⲟⲧⲡⲣⲁⲃⲗⲉⲏⲏⲁя ⲃ ⲙⲟⲣⲅ ⲡⲟⲥⲗⲉ ⲥⲧыⳡⲕυ ⲥ ⲙⲟⲉύ ⳅⲩяⲣⲟύ ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲉⳝⲉ ⳝⲉⳅ  ⲱⲁⲏⲥⲟⲃ ⲧⲩⲧ ⲡⲟ ⲡⲣⲟⲥⲧⲩ ⲏⲉ ⲃыⲯυⲧь ⲧы ⲯⲉ ⲅⲁⲃⲏⲟⲙⲁⲭυⲟⲏⲏⲁя ⲉⳝⲁⲏⲏⲁя ⲧⲉⲗⲕⲁ ⲕⲟⲧⲟⲣⲟύ ⲗυⲱь ⲏⲁⲇⲟ ⲉⳝⲁⲧь ⲣⲃⲇυⳃⲉ  я ⲧⲉⳝⲉ ⲡⲣⲟⲥⲧⲟ ⲡⲉⲣⲉⲗⲟⲙⲁю ⲏⲉ ⲡⲣⲟⲥⲧⲟ ⳡⲧⲟ ⳝы ⲏⲟⲅυ ⲏⲟ υ ⲣⲩⲕυ ⳡⲧⲟ ⳝы ⲧы ⳝⲟⲗьⲱⲉ ⲏⲉ ⲥⲙⲟⲅⲗⲁ ⳡⲧⲟ ⲗυⳝⲟ ⲡⲣυⲙⲉⲏυⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲧⲁⲙ ⲧы ⲯⲉ ⲧⲉⲗⲕⲁ ⲕⲟⲧⲟⲣⲁя ⲡⲟⲇⲩⳡυⲗⲁ ⲡⲟ ⲉⳝⲁⲗⲩ ⲇⲩⲙⲁⲉⲧ ⳡⲧⲟ ⲥⲙⲟⲯⲉⲧ ⲇⲁⲧь ⲧⲉⲡⲉⲣь ⲟⲧⲡⲟⲣ ⲏⲁ ⲥⲃⲟυ ⲅⲁⲃⲏⲟ ⲙⲁⲭυⲏⲁцυυ ⲕⲟⲧⲟⲣыύ ⲟⲏⲁ ⲏⲁⳡυⲏⲁⲗⲁ ⲧⲩⲧ ⲙⲏⲉ ⲃыⲡυⲥыⲃⲁⲧь я ⲧⲉⳝⲉ ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲡⲉⲣⲉⲗⲟⲙⲁю ⲃⲥⲉ ⲧⲃⲟυ ⲕⲟⲥⲧяⲱⲕυ","ⲥыⲏⲩⲗя ⲱⲗюⲭυ ⲏⲉ υⲙⲉюⳃυⲙυ ⲙυⲏυⲙⲁⲗьⲏⲟⲅⲟ ⲥⲟⲥⲧⲁⲃⲗяюⳃⲉⲅⲟ ⲅⲣⲁⲙⲟⲧⲏⲟⲥⲧυ ёⳝⲁⲏⲁя ⲣⲁⳝы ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲟⲧⲟⲣⲁя ⲣⲁⳅⲩⲙⲉⲉⲧⲥя ⲥυⲇυⲧ ⲥⲩⲕⲁ υ ⲥⲃⲟυⲙυ ⲯυⲣⲏыⲙυ ⲕⲟⲡыⲧⲁⲙυ ⲭⲩяⲣυⲧ ⲡⲟ ⲕⲗⲁⲃυⲁⲧⲩⲣⲉ ⲃ ⲏⲁⲇⲉⲯⲇы ⲏⲁ ⲇⲁⲗьⲏⲉύⲱⲉⲉ ⲙⲟё ⲃⲏυⲙⲁⲏυⲉ ёⳝⲁⲏыύ ⲣⲁⲙⲁ ⲉⲅⲟ ⲭⲩύ ⲏυⲕⲟⲙⲩ ⲏⲉυⳅⲃⲉⲥⲧⲏⲟύ ⲇⲉⲅⲉⲏⲉⲣⲁⲧυⲃⲏыύ ⲥыⲏ ⲗⲉⲯⲁⲗⲟⲃⲁ ⲉⳝⲩⳡυⲉ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲣⲁⳅⲩⲙⲉⲉⲧⲥя ⲥⲟ ⲥⲃⲟυⲙ ⲡⲟⲗⲟⲃыⲙ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⳝыⲗ ⲡⲣⲟⲥⲧⲟ ⲣⲁⳅⲣⲉⲯⲩ ⳝⲉⳅ ⲃⲥяⲕⲟⲅⲟ ⲱⲁⲏⲥ ⲏⲁ ⲧⲃⲟύ ⲃыⲯυⲃⲁⲏυⲉ","я ⲧⲉⳝⲉ ⲗυⳡⲏⲟ ⲙⲁⲧь ⲉⳝⲁⲗ ⲧы ⲗυⲱь ⲙⲟя ⲗυⳡⲏⲁя ⲡⲉⲱⲕⲁ ⲏⲉ ⳝⲟⲗⲉⲉ ⲁ ⲏⲩ ⲣⲉⳃⲉ ⲙⲏⲉ ⲡυⲱυ ⳡⲧⲟ ⲗυⳝⲟ ⲥыⲏ ⳝⲗяⲇυ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲃⲟⲃⲥⲉ ⲏⲉ υⳅⲃⲉⲥⲧⲏыύ ⲏυⲕⲟⲙⲩ я ⲧⲉⳝⲉ ⲗυⳡⲏⲟ ⳝⲩⲇⲩ ⲣⲉⳅⲁⲧь ⲅⲗⲁⲏⲇы ⲥыⲏⲕⲩ ⲱⲁⲗⲁⲃы ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲡⲣⲟⲥⲧⲟ ⲇⲉⲅⲉⲏⲉⲣⲁⲧυⲃⲏыύ ⲫⲉⲕⲁⲗьⲏыύ ⲡυⲇⲟⲣⲁⲥ я ⲧⲉⳝⲉ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲉⳝⲗⲁ ⲧⲩⲧ ⲙⲁⲧь ⲃ ⲥⲟⲗⲟ ⲧы ⲥыⲏ ⲭⲩύⲏυ ⲗυⲱь ⲧⲁⲙ ⲙⲉⲇⲗⲉⲏⲏыύ ⲏⲉ ⳝⲟⲗⲉⲉ ⲇⲁⲃⲁύ ⲯⲉ ⲩⲙⲣυ ⲏⲁⲭⲩύ я ⲯⲉ ⲧⲉⳝⲉ ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲃ ⲣыⲗⲟ ⲥⲣⲁⲧь ⲧы ⲡⲟⲏяⲗ ⲙⲉⲏя ⲧⲩⲡⲟύ ⲣⲉⳝⲉⲏⲟⲕ ⲅⲟⲃⲏⲁ ⲏⲁⲭⲩύ","я ⲏⲁⳡⲁⲗ ⲧⲉⳝⲉ ⲗⲟⲙⲁⲧь ⲧⲃⲟυ ⲣⲩⲕυ ⲥыⲏⲕⲩ ⲱⲁⲗⲁⲃы ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲥⲁⲙⲟⲙⲙⲩ ⲥⲗⲁⳝⲟⲙⲩ ⲃⲟⲃⲥⲉ ⲧⲉⳝⲉ ⲏⲉ ⲃыⲯυⲧь ⲃ ⲇⲁⲏⲏⲟύ ⲕⲟⲏⲫⲉⲣⲉⲏцυυ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲧы ⲧⲩⲧ ⳅⲁⲡⲉⲣⲧ ⲥⲟ ⲙⲏⲟύ 1 ⲏⲁ 1 ⲉⳝⲁⲏⲏⲁя ⲱⲩⲱⲃⲁⲗь ⲏⲁⲭⲩύ ⲥⲁⲙⲁя ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲥⲗⲁⳝⲁя ⲇⲉⲅⲉⲏⲉⲣⲁⲧⲕⲁ ⲧы ⲧⲁⲙ ⲥⲃⲟⲉ ⲣыⲗⲟ ⲟⲧⲕⲣыⲗ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⳡⲧⲟⳝы ⲏⲁⳡⲁⲧь ⲙⲏⲉ ⲥⲟⲥυⲣⲟⲃⲁⲧь я ⲏⲉ ⲡⲟύⲙⲩ ⲏⲁⲭⲩύ я  ⲯⲉ ⲧⲉⳝⲉ ⳃⲁⲥ ⲣыⲗⲟ ⲃыⲕⲣⲩⳡⲩ ⲥыⲏⲕⲩ ⳝⲗяⲇυ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲥⲁⲙⲟⲙⲩ ⲥⲗⲁⳝⲟⲙⲩ ⲃⲟⲃⲥⲉ ⲏυⲕⲟⲙⲩ ⲏⲉ ⲏⲩⲯⲏⲟⲙⲩ ⲁ ⲏⲩ ⲣⲉⳃⲉ ⲏⲁⳡυⲏⲁύ ⲙⲏⲉ ⳡⲧⲟ ⲗυⳝⲟ ⲡυⲥⲁⲧь ⲕⲟⲡⲣⲟⲫυⲗьⲏⲁя ⲧⲉⲗⲟⳡⲕⲁ ⲧⲁⲙ ⲯⲉ ⲧⲉⳝⲉ ⲣⲩⲕυ ⳝⲩⲇⲩ ⲗⲟⲙⲁⲧь ⲡⲟⲇ ⲃⲥⲉⲙυ ⲃυⲇⲁⲙυ ⲩⲇⲁⲣⲟⲃ ⲃ ⲧⲃⲟⲉ ⲟⲙⲉⲯⲏⲟⲉ υ ⲧⲁⲕ ⲩⲯⲉ ⲅⲣяⳅⲏⲟⲉ ⲣыⲗьцⲉ ⲏⲁⲭⲩύ"]

state = True
state1 = True
state2 = True
shapka = ""

prem = "[<emoji document_id=5449674274346379447>😈</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5215703418340908982>💎</emoji>]<emoji document_id=6023579014302534620>🔥</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5460898999575785614>❤️</emoji>"
prem2 = "<emoji document_id=5458654823329050591>❤️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6023579014302534620>🔥</emoji>[<emoji document_id=5215703418340908982>💎</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5449674274346379447>😈</emoji>]"
prem2 = "<emoji document_id=5458654823329050591>❤️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6023579014302534620>🔥</emoji>[<emoji document_id=5215703418340908982>💎</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5449674274346379447>😈</emoji>]"

def input_api_credentials():
    print("\033[95mВведите данные API пользователя.\033[0m")
    api_id = input("\033[95mAPI ID: \033[0m")
    api_hash = input("\033[95mAPI Hash: \033[0m")
    return api_id, api_hash

def save_session_credentials(api_id, api_hash):
    with open('sessioncash.txt', 'w') as file:
        file.write(f"{api_id}\n{api_hash}")

def load_session_credentials():
    try:
        with open('sessioncash.txt', 'r') as file:
            api_id = int(file.readline().strip())
            api_hash = file.readline().strip()
            return api_id, api_hash
    except FileNotFoundError:
        return None, None

api_id, api_hash = load_session_credentials()
if not api_id or not api_hash:
    api_id, api_hash = input_api_credentials()
    save_session_credentials(api_id, api_hash)

client = TelegramClient('ocrestrinatedub.session', api_id, api_hash)

version_check_url = "https://raw.githubusercontent.com/Walidname113/KRAVIENCEhelp/main/version.txt"

updates_info_url = "https://raw.githubusercontent.com/Walidname113/KRAVIENCEhelp/main/whats_new.txt"

metabanner = "https://raw.githubusercontent.com/Walidname113/KRAVIENCEhelp/main/Picsart_24-06-03_03-53-49-841.jpg"


def load_send_status():
    try:
        with open('send_status.txt', 'r') as file:
            return file.readline().strip() == 'on'
    except FileNotFoundError:
        return False
        
def save_send_status(status):
    with open('send_status.txt', 'w') as file:
        file.write('on' if status else 'off')

def load_autosend_status():
    try:
        with open('autosend_status.txt', 'r') as file:
            return file.readline().strip() == 'on'
    except FileNotFoundError:
        return False
        
def save_autosend_status(status):
    with open('autosend_status.txt', 'w') as file:
        file.write('on' if status else 'off')
        
def load_chat_ids():
    try:
        with open('chat_ids.txt', 'r') as file:
            return [int(chat_id.strip()) for chat_id in file.readlines()]
    except FileNotFoundError:
        return []

def save_chat_ids(chat_ids):
    with open('chat_ids.txt', 'w') as file:
        for chat_id in chat_ids:
            file.write(f"{chat_id}\n")

def load_words():
    try:
        with open('words.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_words(words):
    with open('words.json', 'w') as file:
        json.dump(words, file)

def load_interval():
    try:
        with open('interval.txt', 'r') as file:
            return int(file.readline().strip())
    except FileNotFoundError:
        return 1200

def save_interval(interval):
    with open('interval.txt', 'w') as file:
        file.write(str(interval))

def save_command_prefix(prefix):
    with open('command_prefix.txt', 'w') as file:
        file.write(prefix)

def load_command_prefix():
    try:
        with open('command_prefix.txt', 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return "."

def load_tagger_status():
    try:
        with open('tagger_status.txt', 'r') as file:
            return file.readline().strip() == 'on'
    except FileNotFoundError:
        return False

def save_tagger_status(status):
    with open('tagger_status.txt', 'w') as file:
        file.write('on' if status else 'off')

def get_current_version():
    response = requests.get(version_check_url)
    if response.status_code == 200:
        return response.text.strip()
    return None

def get_update_info():
    response = requests.get(updates_info_url)
    if response.status_code == 200:
        return response.text.strip()
    return None
    
def get_banner():
    response = requests.get(metabanner)
    if response.status_code == 200:
        with open("metabanner.jpg", "wb") as file:
            file.write(response.content)
        print("Banner loaded Succesfully.")
        return "metabanner.jpg"
    else:
        print("Banner load Error: ", response.status_code)
        return None
   
get_banner()
   
def get_uptime():
    current_time = datetime.now()
    uptime = current_time - start_time
    return uptime
    
@client.on(events.NewMessage(outgoing=True))
async def handle_commands(event):
    import time
    command_prefix = load_command_prefix()
    command = event.message.message
    if not command.startswith(command_prefix):
        return
    command = command[len(command_prefix):].strip()
    chat_id = event.chat_id
    if command.startswith('onsend'):
        send_enabled = load_send_status()
        if send_enabled:
            await event.message.edit('<i><b>Отправка уже включена!</i></b>', parse_mode='HTML')
            time.sleep(5)
            await event.delete()
        else:
            await event.message.edit('<i><b>Отправка включена.</i></b>', parse_mode='HTML')
            save_send_status(True)
            time.sleep(5)
            await event.delete()
    elif command.startswith('offsend'):
        send_enabled = load_send_status()
        if not send_enabled:
            await event.message.edit('<i><b>Отправка уже выключена</i></b>', parse_mode='HTML')
            time.sleep(5)
            await event.delete()
        else:
            await event.message.edit('<i><b>Отправка выключена</i></b>', parse_mode='HTML')
            save_send_status(False)
            time.sleep(5)
            await event.delete()
    elif command.startswith('updateids'):
        vidos = ["https://t.me/Mrakozniyfile/25"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        if chat_id < 0:
            chat_ids = load_chat_ids()
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)
                save_chat_ids(chat_ids)
                await event.delete()
                await event.client.send_file(event.to_id, random_video, caption='<i><b>Ч</b>ᴀᴛ <b>У</b>ᴄᴨᴇ<b>ШН</b>ᴏ <b>Д</b>ᴏ<b>Б</b>ᴀʙᴧᴇ<b>Н</b> ʙ ᴄᴨ<b>И</b>ᴄᴏᴋ.</i>', parse_mode='HTML', supports_streaming=True)
            else:
                await event.message.edit('<i><b>Этот чат уже сохранён в базе.</i></b>', parse_mode='HTML')
        else:
            await event.message.edit('<i><b>Команда доступна только для групп и супергрупп.</i></b>', parse_mode='HTML')
    elif command.startswith('setprefix'):
        vidos = ["https://t.me/Mrakozniyfile/24"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        new_prefix = command[len('setprefix'):].strip()
        if new_prefix and len(new_prefix) == 1 and not new_prefix.isspace() and not new_prefix.isalpha():
            save_command_prefix(new_prefix)
            await event.delete()
            await event.client.send_file(event.to_id, random_video, caption=f'<i><b>П</b>ᴩᴇ<b>ФИ</b>ᴋᴄ <b>У</b>ᴄᴨᴇ<b>ШН</b>ᴏ <b>И3</b>ʍᴇ<b>НЁН Н</b>ᴀ <b>{new_prefix}</b></i>', parse_mode='HTML', supports_streaming=True)
        else:
            await event.message.edit('<i><b>Н</b>ᴇʙᴇᴩ<b>НЫЙ Ф</b>ᴏᴩʍᴀᴛ ᴨᴩᴇ<b>ФИ</b>ᴋᴄᴀ</i>', parse_mode='HTML')
    elif command.startswith('settime'):
        try:
            vidos = ["https://t.me/Mrakozniyfile/21"]
            vidos = list(filter(None, vidos))
            random_video = random.choice(vidos)
            new_interval = int(command[len('settime'):].strip())
            if new_interval > 0:
                save_interval(new_interval)
                await event.delete()
                await event.client.send_file(event.to_id, random_video, caption=f'<i><b>ИН</b>ᴛᴇᴩʙᴀᴧ <b>У</b>ᴄᴨᴇ<b>ШН</b>ᴏ <b>U3</b>ʍᴇ<b>НЁН</b> Нᴀ <b>{new_interval}</b> ᴄᴇᴋ<b>УHD.</b></i>', parse_mode='HTML', supports_streaming=True)
            else:
                await event.message.edit('<i><b>UH</b>ᴛᴇᴩʙᴀᴧ <b>D</b>ᴏᴧ<b>Ж</b>ᴇ<b>H</b> <b>БЫ</b>ᴛ<b>Ь</b> ᴨᴏᴧᴏ<b>ЖИ</b>ᴛᴇᴧ<b>ЬНЫ</b>ʍ ЧИᴄᴧᴏʍ!</i>', parse_mode='HTML')
        except ValueError:
            await event.message.edit('<i><b>H</b>ᴇʙᴇᴩ<b>НЫЙ Ф</b>ᴏᴩʍᴀᴛ <b>ИН</b>ᴛᴇᴩʙᴀᴧᴀ!</i>', parse_mode='HTML')
    elif command.startswith('except'):
        vidos = ["https://t.me/Mrakozniyfile/22"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        chat_ids = load_chat_ids()
        if chat_id in chat_ids:
            chat_ids.remove(chat_id)
            save_chat_ids(chat_ids)
            await event.delete()
            await event.client.send_file(event.to_id, random_video, caption='<i><b>Ч</b>ᴀᴛ <b>У</b>ᴄᴨᴇ<b>ШН</b>ᴏ <b>И</b>ᴄᴋᴧ<b>ЮЧЁН U3</b> ᴄᴨ<b>U</b>ᴄᴋᴀ.</i>', parse_mode='HTML', supports_streaming=True)
        else:
            await event.message.edit('<i><b>Э</bᴛᴏᴛ <b>4</b>ᴀᴛ ᴇ<b>ЩЁ</b> <b>Н</b>ᴇ ᴄᴏ<b>Х</b>ᴩᴀ<b>НЁН</b> ʙ <b>Б</b>ᴀ<b>3</b>ᴇ.</i>', parse_mode='HTML')
    elif command.startswith('removedb'):
        try:
            vidos = ["https://t.me/Mrakozniyfile/23"]
            vidos = list(filter(None, vidos))
            random_video = random.choice(vidos)
            os.remove("chat_ids.txt")
            await event.delete()
            await event.client.send_file(event.to_id, random_video, caption='<i><b>Б</b>ᴀ<b>3</b>ᴀ <b>Ч</b>ᴀᴛᴏʙ <b>У</b>ᴄᴨᴇ<b>ШН</b>ᴏ <b>УД</b>ᴀᴧᴇ<b>Н</b>ᴀ.</i>', parse_mode='HTML', supports_streaming=True)
        except Exception:
            await event.message.edit("<i><b>Н</b>ᴇ <b>УД</b>ᴀᴧᴏᴄ<b>Ь</b> <b>УД</b>ᴀᴧ<b>И</b>ᴛ<b>Ь Б</b>ᴀ<b>3У Д</b>ᴀ<b>ННЫХ Ч</b>ᴀᴛᴏʙ.</i>", parse_mode='HTML')

            
    elif command.startswith('help'):
        vidos = ["https://t.me/Mrakozniyfile/6", "https://t.me/Mrakozniyfile/13", "https://t.me/Mrakozniyfile/16"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        prefix = load_command_prefix()
        await event.edit("[🎭]")
        time.sleep(0.1)
        await event.edit("[🎭]  [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] K 💎 [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KV 💎  [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVA 💎  [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVAR 💎  [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARC 💎 E [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCE 💎 Eb [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCEV 💎 Eba [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCEVIE 💎 Ebas [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCEVIE 💎 Ebash [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCEVIE 💎 Ebashi [🎭]")
        time.sleep(0.1)
        await event.edit("[🎭] KVARCEVIE 💎 Ebashit [🎭]")
        time.sleep(0.5)
        await event.delete()
        time.sleep(0.1)
        await event.client.send_file(event.to_id, random_video, caption=f"<emoji document_id=5388994705805549866>👹</emoji><b>KV</b>ᴀRᴄᴇ<b>Vi</b>ᴇ<emoji document_id=5388994705805549866>👹</emoji>\n\n<b>⛤ |</b> <i>𝑫𝑬𝑫𝑰𝑲</i> <b>| ⛤</b>\n<code>{prefix}onsend</code> <i><b>—</i></b> <i>ʙᴋᴧ<b>ЮЧИ</b>ᴛ<b>Ь</b> <b>D</b>ᴇ<b>DU</b>ᴋ ᴨᴏ <b>Б</b>ᴀ<b>3</b>ᴇ <b>D</b>ᴀ<b>ННЫX</b> <b>Ч</b>ᴀᴛᴏʙ</i>.\n<code>{prefix}offsend</code> <i><b>—</i></b> <i>ʙ<b>Ы</b>ᴋᴧ<b>ЮЧИ</b>ᴛ<b>Ь</b> <b>D</b>ᴇ<b>DU</b>ᴋ.</i>\n<code>{prefix}info</code> <i><b>—</i></b> <i><b>ИНФ</b>ᴏᴩʍᴀ<b>ЦИЯ</b> ᴏ <b>ЮЗᴇ</b>ᴩ<b>Б</b>ᴏᴛᴇ.</i>\n<code>{prefix}uinfo</code> <i><b>—</i></b> <i><b>ИНФ</b>ᴏᴩʍᴀ<b>ЦИЯ</b> ᴏ ᴨᴏᴧ<b>ЬЗ</b>ᴏʙᴀᴛᴇᴧᴇ</i>\n<code>{prefix}loadmedia</code> <i><b>—</i></b> <i><b>3</b>ᴀᴦᴩ<b>У3И</b>ᴛ<b>Ь</b> ʍᴇ<b>DU</b>ᴀ-ɸᴀ<b>Й</b>ᴧ <b>Н</b>ᴀ</i> telegra.ph\n<code>{prefix}cid</code> <i><b>—</i></b> <i><b>УЗН</b>ᴀ<b>Ё</b>ᴛ <b>ID Ч</b>ᴀᴛᴀ, ʙ ᴋᴏᴛᴏᴩᴏʍ Иᴄᴨᴏᴧ<b>ЬЗУ</b>ᴇᴛᴄ<b>Я</b></i>\n\n<b>⛤ |</b> <i>𝑫𝑩</i> <b>| ⛤</b>\n<code>{prefix}updateids</code> <i><b>—</i></b> <i><b>D</b>ᴏ<b>Б</b>ᴀʙ<b>U</b>ᴛ<b>Ь</b> ᴀ<b>ЙDU</b> <b>Ч</b>ᴀᴛᴀ <b>Д</b>ᴧ<b>Я</b> ᴏᴛᴨᴩᴀʙᴋ<b>U</b> ᴄᴏᴏ<b>БЩ</b>ᴇ<b>НИЙ</b> ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>D</b>ᴀ<b>ННЫХ</b>.</i>\n<code>{prefix}removedb</code> <i><b>—</i></b> <i><b>УD</b>ᴀᴧ<b>U</b>ᴛ<b>Ь</b> <b>Б</b>ᴀ<b>3У</b> <b>D</b>ᴀ<b>ННЫХ</b> <b>Ч</b>ᴀᴛᴏʙ.</i>\n<code>{prefix}except</code> <i><b>—</i></b> <i><b>D</b>ᴏ<b>Б</b>ᴀʙ<b>И</b>ᴛ<b>Ь</b> <b>И</b>ᴄᴋᴧ<b>ЮЧ</b>ᴇ<b>НИ</b>ᴇ <b>УЖ</b>ᴇ <b>Д</b>ᴏ<b>Б</b>ᴀʙᴧᴇ<b>НН</b>ᴏᴦᴏ <b>Ч</b>ᴀᴛᴀ ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>Д</b>ᴀ<b>ННЫХ</b>. Ꮶᴏʍᴀ<b>НДУ</b> ʙ<b>ЫЗЫ</b>ʙᴀᴛ<b>Ь</b> ᴛᴏᴧ<b>Ь</b>ᴋᴏ ʙ <b>Ч</b>ᴀᴛᴇ, ᴋᴏᴛᴏᴩ<b>ЫЙ</b> ʙ<b>Ы</b> <b>Д</b>ᴏ<b>Б</b>ᴀʙᴧ<b>Я</b>ᴧ<b>И</b> ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>Д</b>ᴀ<b>ННЫХ</b>.</i>\n\n<b>⛤ |</b> <i>𝑷𝑹𝑬𝑭𝑰𝑿</i> <b>| ⛤</b>\n<code>{prefix}setprefix</code> <i><b>—</i></b> <i><b>U3</b>ʍᴇ<b>HU</b>ᴛ<b>Ь</b> ᴨᴩᴇ<b>ФU</b>ᴋᴄ ᴋᴏʍᴀ<b>НДЫ.</b></i>\n\n<b>⛤ |</b> <i>𝑲𝑫</i> <b>| ⛤</b>\n<code>{prefix}settime</code> <i><b>—</i></b> <i><b>U3</b>ʍᴇ<b>HU</b>ᴛ<b>Ь</b> <b>UH</b>ᴛᴇᴩʙᴀᴧ ʍᴇ<b>ЖДУ</b> ᴏᴛᴨᴩᴀʙᴋᴏ<b>Й</b> ᴄᴏᴏ<b>БЩ</b>ᴇ<b>HUЙ</b> ʙ <b>Ч</b>ᴀᴛ<b>Ы</b>.</i>\n\n<b>⛤ |</b> <i>𝑻𝑨𝑮𝑮𝑬𝑹</i> <b>| ⛤</b> \n<code>{prefix}autotag</code> <i><b>—</i></b> <i>ʙᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ᴀʙᴛᴏᴏᴛʙᴇᴛ Нᴀ ᴧ<b>ЮБ</b>ᴏᴇ ᴄᴏᴏ<b>БЩ</b>ᴇ<b>НИ</b>ᴇ ᴏᴛ ᴛᴇ<b>Х,</b> ᴋᴛᴏ ᴛᴇᴦᴀᴇᴛ ʙᴀᴄ ʙ <b>Б</b>ᴀ<b>3</b>ᴇ <b>D</b>ᴀ<b>HHЫX</b> <b>Ч</b>ᴀᴛᴏʙ.</i>\n<code>{prefix}offautotag</code> <i><b>—</i></b> <i>ʙ<b>Ы</b>ᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ᴀʙᴛᴏᴏᴛʙᴇᴛ<b>ЧU</b>ᴋ <b>Н</b>ᴀ ᴧ<b>ЮБ</b>ᴏᴇ ᴄᴏᴏ<b>БЩ</b>ᴇ<b>HU</b>ᴇ.</i>\n<code>{prefix}mtagger</code> <i><b>—</i></b> <i><b>В</b>ᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ʍᴇ<b>DU</b>ᴀ-ᴛᴇᴦᴦᴇᴩ</i><b>\n<code>{prefix}offmtagger</code> <i><b>—</i></b> <i><b>ВЫ</b>ᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ʍᴇ<b>DU</b>ᴀ-ᴛᴇᴦᴦᴇᴩ.</i>", parse_mode='HTML', supports_streaming=True)
        
    elif command.startswith('info'):
        current_version = get_current_version()
        update_inform = get_update_info()
        expected_version = "1.0.1"
        if current_version and current_version != expected_version:
                    await event.edit(f"<b><i>Разработчик:</b></i> @Ocrestrinated\n<b><i>Связь:</i></b> @Ocrestrinated <i><b>или</i></b> @OcrestrinatedBot <i><b>если у вас спамбан.</i></b>\n<i><b>Исходная информация:</i></b> https://github.com/Walidname113/KRAVIENCEhelp/\n\n<i><b>Version: {current_version}</i></b>\n<i><b>Обновите юзербот, по команде в консоли:</i></b>\n<code>cd && cd KRAVIENCEhelp && bash update.sh</code>\n<b><i>{update_inform}</b></i>", parse_mode='HTML')
        else:
           await event.edit(f"<b><i>Разработчик:</b></i> @Ocrestrinated\n<b><i>Связь:</i></b> @Ocrestrinated <i><b>или</i></b> @OcrestrinatedBot <i><b>если у вас спамбан.</i></b>\n<i><b>Исходная информация:</i></b> https://github.com/Walidname113/KRAVIENCEhelp/\n\n<i><b>Version: {current_version}</i></b>\n<b><i>{update_inform}</b></i>", parse_mode='HTML')
           
    elif command.startswith('autotag'):
        vidos = ["https://t.me/Mrakozniyfile/26"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        tagger_enabled = load_tagger_status()
        if tagger_enabled:
            await event.message.edit('<i><b>Автоответчик уже включён.</i></b>')
        else:
            await event.delete()
            await event.client.send_file(event.to_id, random_video, caption='<i><b>А</b>ʙᴛᴏᴏᴛʙᴇᴛ<b>ЧИ</b>ᴋ ʙᴋᴧ<b>ЮЧЁН.</b></i>', parse_mode='HTML', supports_streaming=True)
            save_tagger_status(True)
            
    elif command.startswith('offautotag'):
        tagger_enabled = load_tagger_status()
        vidos = ["https://t.me/Mrakozniyfile/27"]
        vidos = list(filter(None, vidos))
        random_video = random.choice(vidos)
        if not tagger_enabled:
            await event.message.edit('<i><b>Автоответчик уже выключен.</i></b>', parse_mode='HTML')
        else:
            await event.delete()
            await event.client.send_file(event.to_id, random_video, caption='<i><b>А</b>ʙᴛᴏᴏᴛʙᴇᴛ<b>ЧИ</b>ᴋ ʙ<b>Ы</b>ᴋᴧ<b>ЮЧ</b>ᴇ<b>Н.</b></i>', parse_mode='HTML', supports_streaming=True)
            save_tagger_status(False)
            
    elif command.startswith('uinfo'):
        me = await client.get_me()
        uptime = get_uptime()
        prefix = load_command_prefix()
        current_version = get_current_version()
        expected_version = "1.0.1"
        banner = 'metabanner.jpg'
        formatted_uptime = str(uptime).split('.')[0]

        if me.last_name:
            infomessage = f"👑 Владелец\n┏{me.first_name} {me.last_name}\n┗@{me.username}"
            cpinfo = f"┏📱 Платформа: {platform.system()} {platform.release()}\n┗📀 ОЗУ: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB."
        else:
            infomessage = f"👑 Владелец\n┏{me.first_name}\n┗@{me.username}"
            cpinfo = f"┏📱 Платформа: {platform.system()}\n┗📀 ОЗУ: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB."

        if current_version and current_version != expected_version:
            userbot_message = f"┏🔰 Префикс: {prefix}\n┣🔴 Версия: {current_version} unstable."
        else:
            userbot_message = f"┏🔰 Префикс: {prefix}\n┣🟢 Версия: {current_version} stable."

        information = (f"🌘<i><b>KVRC userbot</b></i>🌒\n\n{infomessage}\n💾 Сервер\n{cpinfo}\n"
                       f"🌌 Юзербот\n{userbot_message}\n┗🌗 Аптайм: {formatted_uptime}")

        await event.delete()
        await event.client.send_file(event.to_id, banner, caption=information, parse_mode='HTML', supports_streaming=True)
  
    elif command.startswith('cid'):
    	chat_id = event.chat_id 
    	await event.edit(f"<b>Conference ID:</b> <code>{chat_id}</code>", parse_mode='HTML')

    elif command.startswith('mtagger'):
        args = event.raw_text.split(maxsplit=1)
        if len(args) < 2:
            await event.edit("❌️ <i><b>Не все аргументы указаны.</b></i>", parse_mode='HTML')
            return
        args = args[1].split()
        if len(args) < 3:
            await event.edit("❌️ <i><b>Не все аргументы указаны.</b></i>", parse_mode='HTML')
            return
        
        message = await event.message.edit("[<emoji document_id=5449674274346379447>😈</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5215703418340908982>💎</emoji>]<emoji document_id=6023579014302534620>🔥</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5460898999575785614>❤️</emoji> <b>ⲥыⲏ ⲱⲁⲗⲁⲃы ⲧя ⳡⲗⲉⲏⲟⲙ ⲡⲟⲕⲁⲱⲙⲁⲣυⲙ</b> <emoji document_id=5458654823329050591>❤️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6023579014302534620>🔥</emoji>[<emoji document_id=5215703418340908982>💎</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5449674274346379447>😈</emoji>]", parse_mode='HTML')

        global state1
        state1 = True
        
        try:
            user_id = int(args[0])
            sl_time = float(args[1])
            ph_url = args[2]

            if not ph_url.startswith(('http://', 'https://')):
                await event.edit("❌️ <i><b>Некорректный URL медиафайла. URL должен начинаться с http:// или https://.</b></i>", parse_mode='HTML')
                return

            while state1:
                text = random.choice(shablon)
                if event.chat:
                    chat_id = event.chat.id
                    response = requests.get(ph_url)
                    if response.status_code == 200:
                        media_file = BytesIO(response.content)
                        media_file.name = ph_url.split('/')[-1]
                        await event.client.send_file(event.peer_id, media_file, caption=f"{shapka} {prem}<a href='tg://user?id={user_id}'>{text}</a>{prem2}", parse_mode='HTML', supports_streaming=True)
                        await asyncio.sleep(0.1)
                        await asyncio.sleep(sl_time)
                    else:
                        await event.edit("❌️ <i><b>Не удалось загрузить медиафайл.</b></i>", parse_mode='HTML')
                        return
                else:
                    await event.edit("❌️ <i><b>Команда должна быть выполнена в чате.</b></i>", parse_mode='HTML')
                    return
        except ValueError:
            await event.edit("❌️ <i><b>Некорректные аргументы. Проверьте правильность ввода - ID KD LINK</b></i>", parse_mode='HTML')
            return
            
    elif command.startswith('offmtagger'):
        state1 = False
        message = await event.edit("[<emoji document_id=5449674274346379447>😈</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5215703418340908982>💎</emoji>]<emoji document_id=6023579014302534620>🔥</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5460898999575785614>❤️</emoji> <b>ⲇⲩⲭⲟⲙ ⲏⲉ ⲡⲁⲇⲁύ ⲃ ⲥⲗⲉⲇⲩюⳃυύ ⲣⲁⳅ ⲗⲩⳡⲱⲉ ⲟⲧⲥⲟⲥⲉⲱь</b> <emoji document_id=5458654823329050591>❤️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6021745393979624496>🌀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346115985705279280>✨</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5346171210394771668>⭐️</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5343577299256091967>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=6023579014302534620>🔥</emoji>[<emoji document_id=5215703418340908982>💎</emoji>|<emoji document_id=5361538796653386656>🔥</emoji>|<emoji document_id=5449674274346379447>😈</emoji>]", parse_mode='HTML')
        time.sleep(7)
        await event.delete()
     
    elif command.startswith('loadmedia'):
        if event.reply_to_msg_id:
            replied_message = await event.get_reply_message()
            if replied_message.media:
                media = replied_message.media
                response = await event.client.download_media(media, file=bytes)

                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                    temp_file.write(response)
                    temp_file_path = temp_file.name
                    
                with open(temp_file_path, 'rb') as file:
                    upload_response = telegraph.upload_file(file)
                file_url = f"https://telegra.ph{upload_response[0]['src']}"
                await event.edit(f"<i><b>Ссылка на медиа: </b></i> <a href='{file_url}'>{file_url}</a>", parse_mode='HTML')
            else:
                await event.edit("❌️ <i><b>Ответ не содержит медиафайлов.</b></i>", parse_mode='HTML')
        else:
            await event.edit("❌️ <i><b>Команда должна быть ответом на сообщение с медиафайлом.</b></i>", parse_mode='HTML')

    elif command.startswith('autosend'):
        try:
            _, chat_id = command.split(' ', 1)
            chat_id = int(chat_id)
            autosend_enabled = load_autosend_status()
            if autosend_enabled:
                await event.message.edit('<i><b>Отправка уже включена!</i></b>', parse_mode='HTML')
            else:
                await event.message.edit('<i><b>Отправка включена.</i></b>', parse_mode='HTML')
                save_autosend_status(True)
        except ValueError:
            await event.message.edit('<i><b>Ошибка: неправильно указан chat_id!</i></b>', parse_mode='HTML')
            return

    elif command.startswith('offautosend'):
        autosend_enabled = load_autosend_status()
        if not autosend_enabled:
            await event.message.edit('<i><b>Отправка уже выключена</i></b>', parse_mode='HTML')
        else:
            await event.message.edit('<i><b>Отправка выключена</i></b>', parse_mode='HTML')
            save_autosend_status(False)
            
@client.on(events.NewMessage(incoming=True))
async def handle_tagged_messages(event):
    tagged_users = {}
    chat_id = event.chat_id
    chat_ids = load_chat_ids()
    if chat_id in chat_ids:
        entities = event.message.entities or []
        user = await event.client.get_entity(event.message.from_id)
        username = user.username if user.username else user.first_name
        mentioned = any(isinstance(entity, MessageEntityMention) and entity.offset == 0 and entity.length >= len(username) for entity in entities)
        replied_to_me_directly = event.is_reply
        if mentioned or replied_to_me_directly:
            now = datetime.now()
            if username in tagged_users:
                tagged_users[username].append(now)
            else:
                tagged_users[username] = [now]
            if len(tagged_users[username]) > 5 and now - tagged_users[username][-5] <= timedelta(seconds=12):
                tagged_users[username] = [] 
                await asyncio.sleep(30)
                return
            tagger_enabled = load_tagger_status()
            if tagger_enabled:
                words = load_words()
                if words:
                    message = random.choice(words)
                    await event.reply(message)
                                                                                       
async def send_random_message(client, words, interval):
    while True:
        if load_send_status():
            chat_ids = load_chat_ids()
            if chat_ids:
                random_word = random.choice(words)
                for chat_id in chat_ids:
                    try:
                        await client.send_message(chat_id, random_word)
                        await asyncio.sleep(interval)                       
                    except telethon.errors.FloodWaitError as e:
                        print(f"Flood wait error: {e}")
                    except Exception as e:
                        print(f"\033[0;31mНе удалось отправить сообщение в чат с ID {chat_id}: {e}\033[0m")
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            print("Cancellation requested. Exiting send_random_message loop.")

async def autosend_random_message(client, words, interval, chat_id):
    while True:
        if load_autosend_status():
            try:
                random_word = random.choice(words)
                await client.send_message(chat_id, random_word)
                await asyncio.sleep(interval)                       
            except telethon.errors.FloodWaitError as e:
                print(f"Flood wait error: {e}")
            except Exception as e:
                print(f"\033[0;31mНе удалось отправить сообщение в чат с ID {chat_id}: {e}\033[0m")
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            print("Cancellation requested. Exiting send_random_message loop.")

print("Start of main function")

async def main(chat_id=None):
    print("Starting Telegram client...")
    await client.start()
    print("Telegram client started.")
    interval = load_interval()
    print("Loaded interval:", interval)
    words = load_words()
    print("Loaded words: Successfully")
    print("Creating task to send random messages...")
    asyncio.create_task(send_random_message(client, words, interval))
    words = load_words()
    print("Task created.")        
    if chat_id is not None:
        print("Running Telegram client...")
        print("Creating task 2 to send random messages and retry load words/interval...")
        interval = load_interval()
        words = load_words()
        asyncio.create_task(autosend_random_message(client, words, interval, chat_id))
        print("Task 2 created.")
    else:
        print("CHAT_ID = NONE. Не создана задача для отправки случайных сообщений вне db. [НЕ КРИТИЧНО]")
    
    print('\033[0;32mНе беспокойся! Всё нормально, это просто логи!\033[0m')
    while True:
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("KeyboardInterrupt detected. Stopping the client.")
            await client.disconnect()
            break

if __name__ == "__main__":
    print("Starting event loop...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Event loop finished.")