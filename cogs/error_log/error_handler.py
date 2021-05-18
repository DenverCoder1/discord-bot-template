import traceback
from datetime import datetime

from discord import logging
from discord.ext.commands import errors


class ErrorHandler:
    """
    Handles different types of error messages
    """

    def __init__(self, message, error, human_details):
        self.message = message
        self.error = error
        self.human_details = human_details
        # formats the error as traceback
        self.trace = traceback.format_exc()

    async def handle_error(self):
        """When an exception is raised, log it in err.log and bot log channel"""
        error_details = self.trace if self.trace != "NoneType: None\n" else self.error
        # logs error as warning in console
        logging.warning(error_details)
        # log to err.log
        self.__log_to_file("err.log", error_details)
        # notify user of error
        user_error = self.__user_error_message()
        if user_error:
            await self.message.channel.send(user_error)

    def __user_error_message(self):
        if isinstance(self.error, errors.CommandNotFound):
            pass  # ignore command not found
        elif isinstance(self.error, errors.MissingRequiredArgument):
            return f"Missing required argument **{self.error.param.name}**."
        elif isinstance(self.error, errors.TooManyArguments):
            return f"Too many arguments given."
        elif isinstance(self.error, errors.BadArgument):
            return f"Bad argument: {self.error}"
        elif isinstance(self.error, errors.NoPrivateMessage):
            return f"That command cannot be used in DMs."
        elif isinstance(self.error, errors.MissingPermissions):
            return (
                "You are missing the following permissions required to run the"
                f' command: {", ".join(self.error.missing_perms)}.'
            )
        elif isinstance(self.error, errors.DisabledCommand):
            return f"That command is disabled or under maintenance."
        elif isinstance(self.error, errors.CommandInvokeError):
            return f"Error while executing the command."
        elif isinstance(self.error, errors.MissingRole):
            role_id = int("".join(filter(lambda x: x.isdigit(), str(self.error))))
            if role_id and self.message and self.message.guild:
                role_name = self.message.guild.get_role(role_id)
                return f"{role_name} role is required to use this command."
            return self.error

    def __log_to_file(self, filename: str, text: str):
        """appends the date and logs text to a file"""
        with open(filename, "a", encoding="utf-8") as f:
            # write the current time and log text at end of file
            f.write(f"{datetime.now()}\n{text}\n------------------------------------\n")
