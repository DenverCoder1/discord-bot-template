import os

import nextcord
from nextcord.ext import commands

import config


def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    # these need to be enabled in the developer portal as well
    intents = nextcord.Intents.default()

    # To enable guild intents:
    # intents.guilds = True

    # To enable member intents:
    # intents.members = True

    # Set custom status to "Listening to ?help"
    activity = nextcord.Activity(
        type=nextcord.ActivityType.listening, name=f"{config.BOT_PREFIX}help"
    )

    bot = commands.Bot(
        commands.when_mentioned_or(config.BOT_PREFIX),
        intents=intents,
        activity=activity,
    )

    # Get the modules of all cogs whose directory structure is cogs/<module_name>/cog.py
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")

    @bot.event
    async def on_ready():
        """When discord is connected"""
        print(f"{bot.user.name} has connected to Discord!")

    # Run Discord bot
    bot.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    main()
