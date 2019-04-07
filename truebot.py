"""Implementation of the main functionality of TrueBot"""
from discord import Game
from discord.ext.commands import Bot
import config

TRUEBOT = Bot(command_prefix=config.BOT_PREFIX)


@TRUEBOT.event
async def on_ready():
    """Function to run when the bot comes online"""
    await TRUEBOT.change_presence(game=Game(name="with humans"))
    print("Logged in as " + TRUEBOT.user.name)

# pylint doesn't like us catching all exceptions here, tough luck
# pylint: disable=broad-except
if __name__ == "__main__":
    for extension in config.EXTENSION_LIST:
        try:
            TRUEBOT.load_extension(extension)
        except Exception as err:
            exc = '{}: {}'.format(type(err).__name__, err)
            print('Failed to load extension {}\n{}'.format(extension, exc))

TRUEBOT.run(config.TOKEN)
