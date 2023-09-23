import sys
from discord.ext import commands

sys.path.append('../')

class sample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)

async def setup(bot):
    await bot.add_cog(sample(bot))