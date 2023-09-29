import os
import sqlite3

class create:
    def setup_main_database():
        # Создаем подключение к базе данных Main
        conn_main = sqlite3.connect('main.db')
        cursor_main = conn_main.cursor()

        # Создаем таблицу Eggs, если она ещё не существует
        cursor_main.execute('''CREATE TABLE IF NOT EXISTS Eggs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Player INTEGER,
                                Player2 INTEGER,
                                egg_id INTEGER
                            )''')

        # Создаем таблицу Pet, если она ещё не существует
        cursor_main.execute('''CREATE TABLE IF NOT EXISTS Pet (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Player INTEGER,
                                Player2 INTEGER,
                                egg_id INTEGER,
                                lvl INTEGER
                            )''')

        # Создаем таблицу User, если она ещё не существует
        cursor_main.execute('''CREATE TABLE IF NOT EXISTS User (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Player INTEGER,
                                lvl INTEGER
                            )''')

        # Сохраняем изменения и закрываем соединение с базой данных Main
        conn_main.commit()
        conn_main.close()

    def setup_inventory_database():
        # Создаем подключение к базе данных Inventory
        conn_inventory = sqlite3.connect('inventory.db')
        cursor_inventory = conn_inventory.cursor()

        # Закрываем соединение с базой данных Inventory
        conn_inventory.close()
