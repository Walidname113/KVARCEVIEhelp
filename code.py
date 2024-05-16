import json
import asyncio
import os
import random
from telethon import TelegramClient, events
import time
import sys

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

def load_send_status():
    try:
        with open('send_status.txt', 'r') as file:
            return file.readline().strip() == 'on'
    except FileNotFoundError:
        return True

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
            await event.message.edit('Отправка уже включена')
        else:
            await event.message.edit('Отправка включена')
            save_send_status(True)
    elif command.startswith('offsend'):
        send_enabled = load_send_status()
        if not send_enabled:
            await event.message.edit('Отправка уже выключена')
        else:
            await event.message.edit('Отправка выключена')
            save_send_status(False)
    elif command.startswith('updateids'):
        if chat_id < 0:
            chat_ids = load_chat_ids()
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)
                save_chat_ids(chat_ids)
                await event.message.edit('Chat_id успешно добавлен в список.')
            else:
                await event.message.edit('Этот чат уже сохранён в базе.')
        else:
            await event.message.edit('Команда доступна только для групп и супергрупп.')
    elif command.startswith('setprefix'):
        new_prefix = command[len('setprefix'):].strip()
        if new_prefix and len(new_prefix) == 1 and not new_prefix.isspace() and not new_prefix.isalpha():
            save_command_prefix(new_prefix)
            await event.message.edit(f'Префикс успешно изменен на {new_prefix}')
        else:
            await event.message.edit('Неверный формат префикса')
    elif command.startswith('settime'):
        try:
            new_interval = int(command[len('settime'):].strip())
            if new_interval > 0:
                save_interval(new_interval)
                await event.message.edit(f'Интервал успешно изменен на {new_interval} секунд')
            else:
                await event.message.edit('Интервал должен быть положительным числом')
        except ValueError:
            await event.message.edit('Неверный формат интервала')
    elif command.startswith('except'):
        chat_ids = load_chat_ids()
        if chat_id in chat_ids:
            chat_ids.remove(chat_id)
            save_chat_ids(chat_ids)
            await event.message.edit('Чат успешно исключен из списка.')
        else:
            await event.message.edit('Этот чат ещё не сохранён в базе.')
    elif command.startswith('removedb'):
        try:
            os.remove("chat_ids.txt")
            await event.message.edit("База чатов успешно удалена.")
        except Exception:
            await event.message.edit("Не удалось удалить базу данных чатов.")
            
    elif command.startswith('help'):
        prefix = load_command_prefix()
        message = event.message.edit
        await message("[🎭]")
        time.sleep(0.1)
        await message("[🎭]  [🎭]")
        time.sleep(0.1)
        await message("[🎭] K 💎 [🎭]")
        time.sleep(0.1)
        await message("[🎭] KV 💎  [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVA 💎  [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVAR 💎  [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARC 💎 E [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCE 💎 Eb [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCEV 💎 Eba [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCEVIE 💎 Ebas [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCEVIE 💎 Ebash [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCEVIE 💎 Ebashi [🎭]")
        time.sleep(0.1)
        await message("[🎭] KVARCEVIE 💎 Ebashit [🎭]")
        time.sleep(1)
        await message(f"KVARCEVIE HELP\n\nDEDIK\nonsend — включить дедик по базе данных чатов.\noffsend — выключить дедик.\n\nDB\nupdateids — добавить айди чата для отправки сообщений в базу данных.\nremovedb — удалить базу данных чатов.\nexcept — добавить исключение уже добавленного чата в базу данных (грубо говоря удалить определённый чат из базы данных, чтобы сообщения туда не отправлялись. Команду вызывать только в чате, который вы добавляли в базу данных.).\n\nPREFIX\nsetprefix — изменить префикс команды.\n\nKD\nsettime — изменить интервал между отправкой сообщений в чаты.\n\nOTHER INFO\nПрефикс команды — {prefix}.\nРазработчик userbot'a: @Ocrestrinated")

async def send_random_message(client, words, interval):
    while True:
        await asyncio.sleep(interval)
        if load_send_status():
            chat_ids = load_chat_ids()
            for chat_id in chat_ids:
                try:
                    message = random.choice(words)
                    await client.send_message(chat_id, message)
                except Exception as e:
                    print(f"\033[0;31mНе удалось отправить сообщение в чат с ID {chat_id}: {e}\033[0m")

async def main():
    await client.start()
    words = load_words()
    interval = load_interval()
    send_task = asyncio.create_task(send_random_message(client, words, interval))
    await send_task

if __name__ == '__main__':
    asyncio.run(main())