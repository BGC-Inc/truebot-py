"""Implementation of the memes class"""
import random
from discord.ext import commands


class Memes(commands.Cog):
    """All the many memes we have for our beautiful bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      brief="Answers from the beyond.",
                      description="Answers a yes/no question.",
                      aliases=['eight_ball', 'eightball', '8-ball'])
    async def eight_ball(self, ctx):
        """Magic eight ball"""
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
        ]
        await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

    @commands.command(name="ihop",
                      brief="I'm down")
    async def ihop(self, ctx):
        """Zach is also down"""
        await ctx.send("I'm down")

    @commands.command(name="ihob",
                      brief="I'm qown")
    async def ihob(self, ctx):
        """Zach is also qown"""
        await ctx.send("I'm qown")

    @commands.command(name="dammit",
                      brief="Slurpee",
                      aliases=["damnit", "dammitslurpee", "damnitslurpee"])
    async def dammit_slurpee(self, ctx):
        """Dollar Sign Dammit Slurpee"""
        await ctx.send("$dammitSlurpee")

    @commands.command(name="false",
                      brief="r/programmerhumor")
    async def funny_because(self, ctx):
        """Get it? Cause ! means not in programmer speak"""
        await ctx.send("It's funny because it's true")

    @commands.command(name="true",
                      brief="I like Star Wars too")
    async def thats_impossible(self, ctx):
        """The quote is actually \"No, I am your father\""""
        await ctx.send("No. No! That's not true! That's impossible!")

    @commands.command(name="done",
                      brief="For when you complete your run",
                      description="But that time is impossible!")
    async def dot_done(self, ctx):
        """Randomly display a meme time from speedrunning history"""
        meme_times = [
            '00:05.51',
            '2:11:18',
            '4:21:09',
            '03:12.40',
            '18:39',
            '47:35',
            '13:37.69',
        ]
        await ctx.send(ctx.message.author.mention + "completed their run in " + random.choice(meme_times) + "!")


def setup(bot):
    """Add this cog to the bot"""
    bot.add_cog(Memes(bot))
