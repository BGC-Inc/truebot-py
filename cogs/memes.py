"""Implementation of the memes class"""
import random
from discord.ext import commands


class Memes():
    """All the many memes we have for our beautiful bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      brief="Answers from the beyond.",
                      description="Answers a yes/no question.",
                      aliases=['eight_ball', 'eightball', '8-ball'],
                      pass_context=True)
    async def eight_ball(self, context):
        """Magic eight ball"""
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
        ]
        await self.bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

    @commands.command(name="ihop",
                      brief="I'm down")
    async def ihop(self):
        """Zach is also down"""
        await self.bot.say("I'm down")

    @commands.command(name="ihob",
                      brief="I'm qown")
    async def ihob(self):
        """Zach is also qown"""
        await self.bot.say("I'm qown")

    @commands.command(name="dammit",
                      brief="Slurpee",
                      aliases=["damnit", "dammitslurpee", "damnitslurpee"])
    async def dammit_slurpee(self):
        """Dollar Sign Dammit Slurpee"""
        await self.bot.say("$dammitSlurpee")

    @commands.command(name="false",
                      brief="r/programmerhumor")
    async def funny_because(self):
        """Get it? Cause ! means not in programmer speak"""
        await self.bot.say("It's funny because it's true")

    @commands.command(name="true",
                      brief="I like Star Wars too")
    async def thats_impossible(self):
        """The quote is actually \"No, I am your father\""""
        await self.bot.say("No. No! That's not true! That's impossible!")

    @commands.command(name="done",
                      brief="For when you complete your run",
                      description="But that time is impossible!",
                      pass_context=True)
    async def dot_done(self, context):
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
        await self.bot.say(context.message.author.mention + "completed their run in " + random.choice(meme_times) + "!")


def setup(bot):
    """Add this cog to the bot"""
    bot.add_cog(Memes(bot))
