import sys
from discord.ext import commands
sys.path.append('../db')  # Добавляем путь к папке db
from db import User
from discord.ext import commands

class EggCreation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(EggCreation(bot))