import discord
from discord.ext import commands
import random

class Misc():

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)


    @commands.command()
    async def anrede(self):
        '''Gives the proper way to adress anybody of power'''
        await self.bot.say ('\n Die Kaiserin wird mit "Euer Kaiserliche Majestät" angesprochen. \n'
                            'Ein König  mit "Euer Königliche Majestät". \n'
                            'Ein Herzog mit "Euer Hoheit". \n'
                            'Ein Fürst mit "Euer Durchlaucht" \n'
                            'Ein Graf mit "Euer Hochwohlgeboren" \n'
                            'Ein Baron oder Freiherr wird mit "Euer Hochgeboren". \n'
                            'Ein Edele, Junker und manchmal Ritter werden mit "Euer Wohlgebore" angeredet. ')

    @commands.command()
    async def anredekirche(self):
        '''Gives the proper way to adress anybody of sacral power'''
        await self.bot.say ('\n Ein Patriarch verdient "Erhabener". \n'
                            'Ein Metropolit, ein Ordensvorsteher und Provinzvorsteher wird mit "Eure Eminenz" angesprochen. \n'
                            'Ein Erzpraetor oder Hoher Tempelvorsteher mit "Euer Exzellenz". \n'
                            'Ein Tempelvorsteher mit "Hochwürden" \n'
                            'Ein Erzpriester mit "Ehrwürden" \n'
                            'Ein Gewiehter mit "Euer Ganden" \n'
                            'Ein Akoluth wird mit "Euer Ehren" angesprochen. ')
