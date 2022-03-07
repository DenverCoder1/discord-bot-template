# Discord Bot Template

[![Discord](https://img.shields.io/discord/819650821314052106?color=7289DA&logo=discord&logoColor=white)](https://discord.gg/fPrdqh3Zfu "Dev Pro Tips Discussion & Support Server")
[![Powered by Nextcord](https://custom-icon-badges.herokuapp.com/badge/-Powered%20by%20Nextcord-0d1620?logo=nextcord)](https://github.com/nextcord/nextcord "Powered by Nextcord Python API Wrapper")

This repo is a template for easy creation of maintainable Python Discord bots.

The library used is [Nextcord](https://github.com/nextcord/nextcord), a maintained fork of Discord.py.

Nextcord documentation: https://nextcord.readthedocs.io/en/latest/

📺 Python Discord Tutorial: https://www.youtube.com/playlist?list=PL9YUC9AZJGFG6larkQJYio_f0V-O1NRjy


## How to use

Click "use this template" at the top of this repo and follow the instructions, or alternatively, initialize a git repo and copy the template files into the directory.

```bash
# Create a new folder (replace my-discord-bot with your bot's name)
mkdir my-discord-bot && cd my-discord-bot
# Initialize the folder as a git repository and copy the template files
git init
cp ../discord-bot-template/* .
```

## Environment variables

To run your bot, you'll need a token and other secrets set in a `.env` file.

Create a file called `.env` and place it in the root of your project.

(You can do this by creating a copy of `.env.sample` and renaming it to `.env`)

The contents should look something like this (where the part after `=` is the token you received from the Discord Developer Portal)

```
DISCORD_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

If you require additional API keys or variables specific to an enviroment, they should also be added here. You can access them by adding a line such as `GUILD_ID = os.getenv("GUILD_ID", "")` to `config.py`.

## Heroku

`runtime.txt` and `Procfile` are used for Heroku configuration and can be deleted in case you do not plan on hosting there.

Heroku setup tutorial: https://www.youtube.com/watch?v=EreE-0hQibM

## IDE Configuration

IDE config such as the `.vscode` folder do not normally belong on GitHub since they are often specific to a particular environment. To make sure GitHub will ignore the `.vscode` folder uncomment the line at the end of the `.gitignore`.

## Coming soon

This repo will eventually contain info on how to use slash commands and other interactions with Nextcord (these features are still in development).
