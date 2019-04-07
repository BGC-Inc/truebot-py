"""Implementation of the utilities class"""
from discord.ext import commands


class Utilities():
    """Utility commands and functionality"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping",
                      brief="Pings the bot")
    async def ping(self):
        """Pings the bot"""
        await self.bot.say("Pong!")

    @commands.command(name="pong",
                      brief="Pongs the bot")
    async def pong(self):
        """Pongs the bot"""
        await self.bot.say("Ping!")

    @commands.command(name="copy",
                      brief="Return to sender",
                      pass_context=True)
    async def copycat(self, context):
        """Repeats the provided message back to the user"""
        await self.bot.say(context.message.content)


def setup(bot):
    """Add this cog to the bot"""
    bot.add_cog(Utilities(bot))
