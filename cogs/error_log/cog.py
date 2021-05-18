import sys

from cogs.error_log.error_handler import ErrorHandler
from discord.ext import commands


class ErrorLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="logs")
    @commands.has_permissions(administrator=True)
    async def logs(self, ctx, num_lines: int = 50):
        """Show recent logs from err.log
        Usage:
        ```
        !logs
        !logs 20
        ```
        Arguments:

        > num_lines (optional): the number of lines to display from the logs
        """
        # log in console that a ping was received
        print('Executing command "logs".')
        # reply with end of log file
        with open("err.log", "r", encoding="utf-8") as f:
            # read logs file
            lines = f.readlines()
            last_n_lines = "".join(lines[-num_lines:])
            # trim the logs if too long
            if len(last_n_lines) > 1990:
                last_n_lines = f"․․․\n{last_n_lines[-1990:]}"
            # send the logs
            await ctx.send(f"```{last_n_lines}```")


async def on_error(event, *args, **kwargs):
    """When an exception is raised, log it in err.log and bot log channel"""
    _, error, _ = sys.exc_info()
    # error while handling message
    if event in [
        "message",
        "on_message",
        "message_discarded",
        "on_message_discarded",
        "on_command_error",
    ]:
        msg = f"**Error while handling a message**"
        await ErrorHandler(args[0], error, msg).handle_error()
    # other errors
    else:
        msg = f"An error occurred during and event and was not reported: {event}"
        await ErrorHandler("", error, msg).handle_error()


async def on_command_error(ctx, error):
    """When a command exception is raised, log it in err.log and bot log channel"""
    details = f"**Error while running command**\n```\n{ctx.message.clean_content}\n```"
    await ErrorHandler(ctx.message, error, details).handle_error()


# setup functions for bot
def setup(bot):
    bot.add_cog(ErrorLog(bot))
    bot.on_error = on_error
    bot.on_command_error = on_command_error
