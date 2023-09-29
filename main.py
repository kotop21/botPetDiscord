import discord
import os
import sqlite3
import sys
from discord.ext import commands
from config import config
from db import User
from db import create
from colorama import Fore, Back, Style, init

init(autoreset=True)# Инициализация Colorama.

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

# bd
create.setup_main_database()
create.setup_inventory_database()

@bot.event 
async def on_ready():
    for filename in os.listdir('./cogs'):  # Проход по файлам в каталоге "cogs"
        if filename.endswith(".py"):  # Если файл является скриптом Python.
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")  # Загрузка коги в бота с использованием 'await'.
                print(Fore.GREEN + f"Loaded {filename[:-3]}")  # Успешная загрузка.
            except Exception as e:
                print(Fore.RED + f'Error loading module {filename}: {str(e)}')  # Ошибка. 

if __name__ == "__main__":
    try:
        bot.run(config.TOKEN)  # Попытка запустить бота с использованием токена из файла конфигурации.
    except discord.HTTPException as e:
        if e.status == 429:
            print(Fore.RED + "Сервера Discord отклонили соединение из-за слишком многих запросов")
            # Если ошибка HTTP 429, выведите сообщение о том, что сервера Discord отклонили соединение из-за слишком многих запросов.
        else:
            raise e  # Если возникла другая ошибка, выведите ее исключение для отладки.
