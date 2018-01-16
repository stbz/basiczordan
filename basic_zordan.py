import discord
from discord.ext import commands

from cogs import dbfunc, misc
import os

description = '''The ZordanBot'''

bot = commands.Bot(command_prefix='?', description=description)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def setup(bot):
    bot.add_cog(misc.Misc(bot))
    bot.add_cog(dbfunc.DBFunc(bot))

def launch():
    dbfunc.DBFunc.ini()

setup(bot)
launch()
bot.run(token=os.environ[BOT_TOKEN])
