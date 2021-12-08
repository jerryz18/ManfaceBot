from discord.ext import commands
from random import choice

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ym', aliases=['yomama'])
    async def yo_mama(self, ctx):
        """Say a Yo Mama joke"""
        await ctx.send(
            f'Yo mama is so {choice(self.bot.adjectives)} she {choice(self.bot.verbs)}!'
        )

    @commands.command(name='yd', aliases=['yodad'])
    async def yo_dad(self, ctx):
        """Say a Yo Dad joke"""
        await ctx.send(
            f'Yo dad is so {choice(self.bot.adjectives)} he {choice(self.bot.verbs2)}!'
        )

    @commands.command(name='dn', aliases=['deeznuts'])
    async def deez_nuts(self, ctx):
        """got em"""
        await ctx.send('DEEZ NUTS IN YO MOUTH. GOTEEEEM')

def setup(bot):
    bot.add_cog(Commands(bot)) 