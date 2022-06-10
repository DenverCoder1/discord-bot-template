from nextcord.ext import commands
from utils.embedder import embed_success


class Ping(commands.Cog, name="Ping"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """A command which simply acknowledges the user's ping.
        Usage:
        ```
        ?ping
        ```
        """
        # log in console that a ping was received
        print("Received ping")
        # respond to the message
        await ctx.send(embed=embed_success("Pong!"))


# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
