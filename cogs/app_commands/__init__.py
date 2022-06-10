import nextcord
from nextcord.ext import commands
from utils import embed_success


class ApplicationCommandsExample(commands.Cog, name="App Commands"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(description="Slash command that responds with 'Hello World'")
    async def my_slash_cmd(self, interaction: nextcord.Interaction):
        await interaction.send(embed=embed_success("Hello World!"))

    @nextcord.slash_command(description="Slash command that repeats an argument")
    async def my_slash_cmd_2(self, interaction: nextcord.Interaction, my_arg: str):
        await interaction.send(embed=embed_success(f"You said: {my_arg}"))

    @nextcord.user_command()
    async def my_user_cmd(self, interaction: nextcord.Interaction, member: nextcord.Member):
        await interaction.send(f"Hello, {member.mention}!")

    @nextcord.message_command()
    async def my_message_cmd(self, interaction: nextcord.Interaction, message: nextcord.Message):
        await interaction.send(f"Hello, {message.author.mention}!")


# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(ApplicationCommandsExample(bot))
