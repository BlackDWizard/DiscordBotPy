# coreImport
import discord
from discord.ext import commands

# customImport
import json
import keepAlive

from normalFunction import normalFunction

with open("setting.json", mode="r", encoding="UTF8") as setting:
    settingDictionary = json.load(setting)

client = commands.Bot(command_prefix='~')  # client 是我們與 Discord 連結的橋樑

client.add_cog(normalFunction(client))

# region logonToken
# TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
keepAlive.keep_alive()
client.run(settingDictionary["TOKEN"])
# endregion
