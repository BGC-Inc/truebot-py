"""Implementation of the utilities class"""
from discord.ext import commands


class Utilities(commands.Cog):
    """Utility commands and functionality"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping",
                      brief="Pings the bot")
    async def ping(self, ctx):
        """Pings the bot"""
        await ctx.send("Pong!")

    @commands.command(name="pong",
                      brief="Pongs the bot")
    async def pong(self, ctx):
        """Pongs the bot"""
        await ctx.send("Ping!")

    @commands.command(name="copy",
                      brief="Return to sender")
    async def copycat(self, ctx):
        """Repeats the provided message back to the user"""
        await ctx.send(ctx.message.content)

    @commands.command(name="say",
                      brief="Put words in my mouth")
    async def say_in_channel(self, ctx, channel: int, message):
        """TrueBot has gained sentience, tell him what to say"""
        target_channel = self.bot.get_channel(channel)
        await target_channel.send(message)

    @commands.command(name="live",
                      brief="Toogle the red dot")
    async def toggle_live(self, ctx):
        """Toggles the red dot in the users voice channel to signify the user is streaming"""
        user_voice_channel = ctx.message.author.voice.channel
        user_name = ctx.message.author.name
        old_name = user_voice_channel.name
        if "🔴" in old_name:
            await user_voice_channel.edit(name=old_name[2:], reason=user_name + " stopped streaming")
        else:
            await user_voice_channel.edit(name="🔴 " + old_name, reason=user_name + " started streaming")


def setup(bot):
    """Add this cog to the bot"""
    bot.add_cog(Utilities(bot))
