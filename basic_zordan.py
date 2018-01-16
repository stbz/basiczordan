import discord
from discord.ext import commands
from boto.s3.connection import S3Connection

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
token = S3Connection(os.environ['BOT_TOKEN'])
bot.run(token)
