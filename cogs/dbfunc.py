import discord
from discord.ext import commands
from tinydb import TinyDB, Query, where
import ast

tindb = TinyDB('db.json')
# gift andrea a novel with cultural background in the 20th century.
class DBFunc():

    def __init__(self, bot):
        self.bot = bot

    def ini():
            #needs to check more cases
        if tindb.table('date'):
            table = tindb.table('date')
            table.update({'date' : '1.Praois'})
        if tindb.table('system'):
            table = tindb.table('system')
            table.update({'init': True })
        if tindb.table('economy'):
            table = tindb.table('economy')
            table.update({'treasury': 0})



    @commands.command()
    async def date(self):
        '''Returns the current Date in Aventurien'''
        date = tindb.table('date')
        dsadate = date.search(where('date').exists())
        await self.bot.say('Es ist der {date}'.format_map(dsadate[0]))

    @commands.command()
    async def setdate(self, *, newdate: str):
        '''Sets the current Date in Aventurien'''
        date = tindb.table('date')
        date.update({ 'date': newdate})
        await self.bot.say('Das neue Datum ist nun {0}'.format(newdate))

    @commands.command(description='Returns info of the current state of the treasury')
    async def gold(self):
        '''Returns the current gold in the treasury and the expected income for the next month'''
        economy = tindb.table('economy')
        treasury = economy.search(where('treasury').exists())
        await self.bot.say('In der Schatzkammer befinden sich {treasury} Dukaten.'.format_map(treasury[0]))


    @commands.command(description='Adds money from the treasury')
    async def plusgold(self, money: int):
        '''Adds money from the treasury'''
        economy = tindb.table('economy')
        treasury = economy.search(where('treasury').exists())
        oldmoney = int('{treasury}'.format_map(treasury[0]))
        newmoney = int('{treasury}'.format_map(treasury[0])) + money
        economy.update({'treasury': newmoney})
        await self.bot.say('Es waren {0} Dukaten in der Schatzkammer und nun sind es {1} Dukaten'.format(oldmoney,newmoney))

    @commands.command(description='Deduct money from the treasury')
    async def minusgold(self, money: int):
        '''Deduct money from the treasury'''
        economy = tindb.table('economy')
        treasury = economy.search(where('treasury').exists())
        oldmoney = int('{treasury}'.format_map(treasury[0]))
        newmoney = int('{treasury}'.format_map(treasury[0])) - money
        economy.update({'treasury': newmoney})
        await self.bot.say('Es waren {0} Dukaten in der Schatzkammer und nun sind es {1} Dukaten'.format(oldmoney,newmoney))

    @commands.command(description='Sets money from the treasury')
    async def setgold(self, money: int):
        '''Sets money from the treasury'''
        economy = tindb.table('economy')
        treasury = economy.search(where('treasury').exists())
        economy.update({'treasury': money})
        await self.bot.say('Es sind nun {0} Dukaten in der Schatzkammer'.format(money))



    @commands.command(description='Set the info of a Town')
    async def settown(self, *, ctx: str):
        '''Sets the info of town: Needs name, barony, ruler, industry, pop, garisson as values'''
        try:
            name, barony, ruler, industry, pop, garisson = map(str, ctx.split(', '))
        except Exception:
            await self.bot.say('Die Felder müssen mit einem , getrennt werden.')
            return
        towns = Query()
        if tindb.search(towns.name.matches(name)):
            await self.bot.say('Die Stadt existiert in meinen Aufzeichnungen schon.')
        else:
            tindb.insert({'name': name, 'barony': barony, 'ruler': ruler, 'industry': industry, 'pop': pop, 'garisson': garisson })
            await self.bot.say('Ich habe {0} meinen Aufzeichnungen hinzugefügt.'.format(name))

    @commands.command(description='Update info of a Town')
    async def updatetown(self, *, ctx: str):
        '''Updates the info of a town'''
        try:
            name, field, value = map(str, ctx.split(', '))
        except Exception:
            await self.bot.say('Die Felder müssen mit einem , getrennt werden.')
            return
        towns = tindb.search(where('name') == name)
        if bool(towns):
            tindb.update({field : value}, doc_ids = [towns[0].doc_id])
            await self.bot.say('Ich habe meine Aufzeichnungen überarbeitet.')
        else:
            await self.bot.say('Diese Stadt existiert in meinen Aufzeichnungen nicht.')

    @commands.command(description='Get the places in a Barony')
    async def barony(self, baronyname: str):
        '''Fetches the info of Barony'''
        towns = tindb.search(where('barony') == baronyname)
        if bool(towns):
            townlist = ', '.join('{name}'.format_map(towns[i]) for i in range(len(towns)))
            await self.bot.say('In der Baronie {0} liegen die Orte: {1}.'.format(baronyname, townlist))
        else:
            await self.bot.say('Die Baronie existiert in meinen Aufzeichnungen nicht.')

    @commands.command(description='Get the info of a ruler')
    async def ruler(self, * ,rulername: str):
        '''Fetches the info of a ruler'''
        towns = tindb.search(where('ruler') == rulername)
        if bool(towns):
            townlist = ', '.join('{name}'.format_map(towns[i]) for i in range(len(towns)))
            troops = ', '.join('{garisson}'.format_map(towns[i]) for i in range(len(towns)))
            await self.bot.say('{0} herrscht über die Orte: {1}. '
                                'Mit jeweils {2} Mann.'.format(rulername, townlist, troops))
        else:
            await self.bot.say('Der Herrscher existiert in meinen Aufzeichnungen nicht.')

    @commands.command(description='Get the Info of a Town')
    async def town(self, *,townname: str):
        '''Fetches the info of town'''
        towns = tindb.search(where('name') == townname)
        if bool(towns):
            townDic = {}
            townDic = towns[0]
            await self.bot.say('{name} liegt in der Baronie {barony}. '
                                'Es leben ungefähr {pop} Menschen in {name}. '
                                'Die Wirtschaft betsteht aus: {industry}. Es herrscht {ruler} '
                                'mit einer geschätzten Truppenstärke von {garisson} Mann.'.format_map(townDic))
        else:
            await self.bot.say('Diese Stadt existiert in meinen Aufzeichnungen nicht.')
