import json
import asyncio
import os
import random
import telethon
from telethon import TelegramClient, events, utils
import time
import sys
import requests
import subprocess

subprocess.run(["clear"])

print("\033[0;32mЮзербот успешно запущен!\033[0m")

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

def load_send_status():
    try:
        with open('send_status.txt', 'r') as file:
            return file.readline().strip() == 'on'
    except FileNotFoundError:
        return False

def save_send_status(status):
    with open('send_status.txt', 'w') as file:
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

@client.on(events.NewMessage(outgoing=True))
async def handle_commands(event):
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
        else:
            await event.message.edit('<i><b>Отправка включена.</i></b>', parse_mode='HTML')
            save_send_status(True)
    elif command.startswith('offsend'):
        send_enabled = load_send_status()
        if not send_enabled:
            await event.message.edit('<i><b>Отправка уже выключена</i></b>', parse_mode='HTML')
        else:
            await event.message.edit('<i><b>Отправка выключена</i></b>', parse_mode='HTML')
            save_send_status(False)
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
            await event.message.edit('<i><b>Э</b>ᴛᴏᴛ <b>4</b>ᴀᴛ ᴇ<b>ЩЁ</b> <b>Н</b>ᴇ ᴄᴏ<b>Х</b>ᴩᴀ<b>НЁН</b> ʙ <b>Б</b>ᴀ<b>3</b>ᴇ.</i>', parse_mode='HTML')
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
        await event.client.send_file(event.to_id, random_video, caption=f"<emoji document_id=5388994705805549866>👹</emoji><b>KV</b>ᴀRᴄᴇ<b>Vi</b>ᴇ<emoji document_id=5388994705805549866>👹</emoji>\n\n<b>⛤ |</b> <i>𝑫𝑬𝑫𝑰𝑲</i> <b>| ⛤</b>\n<code>{prefix}onsend</code> <i><b>—</i></b> <i>ʙᴋᴧ<b>ЮЧИ</b>ᴛ<b>Ь</b> <b>D</b>ᴇ<b>DU</b>ᴋ ᴨᴏ <b>Б</b>ᴀ<b>3</b>ᴇ <b>D</b>ᴀ<b>ННЫX</b> <b>Ч</b>ᴀᴛᴏʙ</i>.\n<code>{prefix}offsend</code> <i><b>—</i></b> <i>ʙ<b>Ы</b>ᴋᴧ<b>ЮЧИ</b>ᴛ<b>Ь</b> <b>D</b>ᴇ<b>DU</b>ᴋ.</i>\n<code>{prefix}info</code> <i><b>—</i></b> <i><b>ИНФ</b>ᴏᴩʍᴀ<b>ЦИЯ</b> ᴏ <b>ЮЗᴇ</b>ᴩ<b>Б</b>ᴏᴛᴇ.</i>\n\n<b>⛤ |</b> <i>𝑫𝑩</i> <b>| ⛤</b>\n<code>{prefix}updateids</code> <i><b>—</i></b> <i><b>D</b>ᴏ<b>Б</b>ᴀʙ<b>U</b>ᴛ<b>Ь</b> ᴀ<b>ЙDU</b> <b>Ч</b>ᴀᴛᴀ <b>Д</b>ᴧ<b>Я</b> ᴏᴛᴨᴩᴀʙᴋ<b>U</b> ᴄᴏᴏ<b>БЩ</b>ᴇ<b>НИЙ</b> ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>D</b>ᴀ<b>ННЫХ</b>.</i>\n<code>{prefix}removedb</code> <i><b>—</i></b> <i><b>УD</b>ᴀᴧ<b>U</b>ᴛ<b>Ь</b> <b>Б</b>ᴀ<b>3У</b> <b>D</b>ᴀ<b>ННЫХ</b> <b>Ч</b>ᴀᴛᴏʙ.</i>\n<code>{prefix}except</code> <i><b>—</i></b> <i><b>D</b>ᴏ<b>Б</b>ᴀʙ<b>И</b>ᴛ<b>Ь</b> <b>И</b>ᴄᴋᴧ<b>ЮЧ</b>ᴇ<b>НИ</b>ᴇ <b>УЖ</b>ᴇ <b>Д</b>ᴏ<b>Б</b>ᴀʙᴧᴇ<b>НН</b>ᴏᴦᴏ <b>Ч</b>ᴀᴛᴀ ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>Д</b>ᴀ<b>ННЫХ</b>. Ꮶᴏʍᴀ<b>НДУ</b> ʙ<b>ЫЗЫ</b>ʙᴀᴛ<b>Ь</b> ᴛᴏᴧ<b>Ь</b>ᴋᴏ ʙ <b>Ч</b>ᴀᴛᴇ, ᴋᴏᴛᴏᴩ<b>ЫЙ</b> ʙ<b>Ы</b> <b>Д</b>ᴏ<b>Б</b>ᴀʙᴧ<b>Я</b>ᴧ<b>И</b> ʙ <b>Б</b>ᴀ<b>ЗУ</b> <b>Д</b>ᴀ<b>ННЫХ</b>.</i>\n\n<b>⛤ |</b> <i>𝑷𝑹𝑬𝑭𝑰𝑿</i> <b>| ⛤</b>\n<code>{prefix}setprefix</code> <i><b>—</i></b> <i><b>U3</b>ʍᴇ<b>HU</b>ᴛ<b>Ь</b> ᴨᴩᴇ<b>ФU</b>ᴋᴄ ᴋᴏʍᴀ<b>НДЫ.</b></i>\n\n<b>⛤ |</b> <i>𝑲𝑫</i> <b>| ⛤</b>\n<code>{prefix}settime</code> <i><b>—</i></b> <i><b>U3</b>ʍᴇ<b>HU</b>ᴛ<b>Ь</b> <b>UH</b>ᴛᴇᴩʙᴀᴧ ʍᴇ<b>ЖДУ</b> ᴏᴛᴨᴩᴀʙᴋᴏ<b>Й</b> ᴄᴏᴏ<b>БЩ</b>ᴇ<b>HUЙ</b> ʙ <b>Ч</b>ᴀᴛ<b>Ы</b>.</i>\n\n<b>⛤ |</b> <i>𝑻𝑨𝑮𝑮𝑬𝑹</i> <b>| ⛤</b> \n<code>{prefix}autotag</code> <i><b>—</i></b> <i>ʙᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ᴀʙᴛᴏᴏᴛʙᴇᴛ Нᴀ ᴧ<b>ЮБ</b>ᴏᴇ ᴄᴏᴏ<b>БЩ</b>ᴇ<b>НИ</b>ᴇ ᴏᴛ ᴛᴇ<b>Х,</b> ᴋᴛᴏ ᴛᴇᴦᴀᴇᴛ ʙᴀᴄ ʙ <b>Б</b>ᴀ<b>3</b>ᴇ <b>D</b>ᴀ<b>HHЫX</b> <b>Ч</b>ᴀᴛᴏʙ.</i>\n<code>{prefix}offautotag</code> <i><b>—</i></b> <i>ʙ<b>Ы</b>ᴋᴧ<b>ЮЧ</b>ᴀᴇᴛ ᴀʙᴛᴏᴏᴛʙᴇᴛ<b>ЧU</b>ᴋ <b>Н</b>ᴀ ᴧ<b>ЮБ</b>ᴏᴇ ᴄᴏᴏ<b>БЩ</b>ᴇ<b>HU</b>ᴇ.</i>\n<b>⛤ |</b> <i>𝑶𝑻𝑯𝑬𝑹 𝑰𝑵𝑭𝑶</i> <b>| ⛤</b>\n<i>Пᴩᴇ<b>ФИ</b>ᴋᴄ ᴋᴏʍᴀ<b>НДЫ —</b></i> <code>{prefix}</code>\nРᴀ<b>3</b>ᴩᴀ<b>Б</b>ᴏᴛ<b>4U</b>ᴋ 𝒖𝒔𝒆𝒓𝒃𝒐𝒕'𝒂: @Ocrestrinated", parse_mode='HTML', supports_streaming=True)
        
    elif command.startswith('info'):
        current_version = get_current_version()
        expected_version = "1.0.0"
        if current_version and current_version != expected_version:
                    await event.edit(f"<b><i>Разработчик:</b></i> @Ocrestrinated\n<b><i>Связь:</i></b> @Ocrestrinated <i><b>или</i></b> @OcrestrinatedBot <i><b>если у вас спамбан.</i></b>\n<i><b>Исходная информация:</i></b> https://github.com/Walidname113/KRAVIENCEhelp/\n\n<i><b>Version: {current_version}</i></b>\n<i><b>Обновите юзербот, по команде в консоли:</i></b>\n<code>cd && cd KRAVIENCEhelp && bash update.sh</code>", parse_mode='HTML')
        else:
           await event.edit(f"<b><i>Разработчик:</b></i> @Ocrestrinated\n<b><i>Связь:</i></b> @Ocrestrinated <i><b>или</i></b> @OcrestrinatedBot <i><b>если у вас спамбан.</i></b>\n<i><b>Исходная информация:</i></b> https://github.com/Walidname113/KRAVIENCEhelp/\n\n<i><b>Version: {current_version}</i></b>", parse_mode='HTML')
           
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
            

@client.on(events.NewMessage(incoming=True))
async def handle_tagged_messages(event):
    chat_id = event.chat_id
    chat_ids = load_chat_ids()
    if chat_id in chat_ids:
        entities = event.message.entities or []
        if event.is_reply or any(entity.user_id == client.get_me().id for entity in entities if hasattr(entity, 'user_id')):
            tagger_enabled = load_tagger_status()
            if tagger_enabled:
                words = load_words()
                if words:
                    message = random.choice(words)
                    await event.reply(message)
 
@client.on(events.NewMessage(incoming=True))
async def handle_tagged_messages(event):
    chat_id = event.chat_id
    chat_ids = load_chat_ids()
    if chat_id in chat_ids:
        entities = event.message.entities or []
        mentioned = any(entity.type == 'mention' and entity.user_id == client.get_me().id for entity in entities)
        replied_to_me_directly = event.is_reply and event.message.reply_to.reply_to_id == client.get_me().id
        if mentioned or replied_to_me_directly:
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
                        print(f"Failed to send message to chat ID {chat_id}: {e}")

                    except Exception as e:
                        print(f"\033[0;31mНе удалось отправить сообщение в чат с ID {chat_id}: {e}\033[0m")

print("Start of main function")

async def main():
    print("Starting Telegram client...")
    await client.start()
    print("Telegram client started.")
    words = load_words()
    print("Loaded words:", words)
    interval = load_interval()
    print("Loaded interval:", interval)
    print("Creating task to send random messages...")
    asyncio.create_task(send_random_message(client, words, interval))
    print("Task created.")
    print("Running Telegram client until disconnected...")
    await client.run_until_disconnected()
    print("Telegram client disconnected.")

if __name__ == "__main__":
    print("Starting event loop...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Event loop finished.")