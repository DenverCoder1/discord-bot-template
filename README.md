# Discord Bot Template

This repo is a template for easy creation of maintainable [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html) bots.

📺 Python Discord Tutorial: https://www.youtube.com/playlist?list=PL9YUC9AZJGFG6larkQJYio_f0V-O1NRjy

<p align="center">
  <a href="https://discord.gg/fPrdqh3Zfu" alt="Discord" title="Dev Pro Tips Discussion & Support Server">
    <img src="https://img.shields.io/discord/819650821314052106?color=7289DA&logo=discord&logoColor=white&style=for-the-badge"/></a>
</p>


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

The contents should look something like this (where the part after `=` is the token you received from the Discord Developer Portal)

```
DISCORD_TOKEN=EXAMPLE_AJKN343NKJAFAN234DFA_LNLDA3DJK24N4
```

If you require additional API keys or variables specific to an enviroment, they should also be added here. You can access them by adding a line such as `GUILD_ID = os.getenv("GUILD_ID", "")` to `config.py`.

## Heroku

`runtime.txt` and `Procfile` are used for Heroku configuration and can be deleted in case you do not plan on hosting there.

## IDE Configuration

IDE config such as the `.vscode` folder do not normally belong on GitHub since they are often specific to a particular environment. To make sure GitHub will ignore the `.vscode` folder uncomment the line at the end of the `.gitignore`.
