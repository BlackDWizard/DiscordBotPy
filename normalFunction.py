# coreImport
import discord
from discord.ext import commands

import json

# variableImport
import random
import math
from datetime import datetime, timezone, timedelta

with open("setting.json", mode="r", encoding="UTF8") as setting:
    settingDictionary = json.load(setting)

client = commands.Bot(command_prefix='~')  # client 是我們與 Discord 連結的橋樑

cmdArray = settingDictionary["cmdArray"]

food = settingDictionary["food"]

cleanText = settingDictionary["cleanText"]

userMentionable = settingDictionary["UserMentionable"]


# region bot action


class normalFunction(commands.Cog):
    def __init__(self, client):

        @client.command()
        async def 乳滑(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send(
                    "https://tenor.com/view/miss-you-we-miss-them-gif-13362284")

        @client.command()
        async def 沒過(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send(file=discord.File('./image/boom.jpg'))

        @client.command()
        async def 過了(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send(file=discord.File('./image/pass.gif'))

        @client.command()
        async def PA(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send(
                    "https://tenor.com/view/worship-pa-pearl-abyss-gif-20263613")

        @client.command()
        async def 大便(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranPopo = math.floor(random.random() * 50) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今天大便最長能拉到 " +
                               str(ranPopo) + " 公分！")

        @client.command()
        async def 尻尻(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranKaokao = math.floor(random.random() * 60) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今天尻尻最久能尻 " +
                               str(ranKaokao) + " 分鐘！")

        @client.command()
        async def 吃啥(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranFood = math.floor(random.random() * len(food))
                await ctx.send("吃" + food[ranFood] + "吧~~")

        @client.command()
        async def dice(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranDice = math.floor(random.random() * 1000000) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 骰出了 " + str(ranDice) + " 點！")

        @client.command()
        async def bdo(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranBdo = math.floor(random.random() * 99) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今天衝裝機率: " +
                               str(ranBdo) + " %！")

        @client.command()
        async def sixtyNine(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + ">, 你又沒對象在69尛")

        @client.command()
        async def bang(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send("誰再雞腿bang當 群主就讓他媽媽復活")

        @client.command()
        async def dick(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranDick = math.floor(random.random() * 30) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今天雞雞最長能硬到 " +
                               str(ranDick) + " 公分！")

        @client.command()
        async def server(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send("```" + "Server name:" +
                               ctx.guild.name +
                               "\nTotal members:" +
                               str(ctx.guild.member_count) +
                               "```")

        @client.command()
        async def 早安(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                await ctx.send("早安啊~" + "<@" + sender +
                               "> 今天也要繼續努力唷~")

        @client.command()
        async def 午安(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                await ctx.send("午安啊~" + "<@" + sender +
                               "> 吃飽了嗎？要堅持住唷~")

        @client.command()
        async def 晚安(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                await ctx.send("晚安啊~" + "<@" + sender +
                               "> 你好嗎？你今天過得好嗎？")

        @client.command()
        async def 福利熊(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send("⣿⣿⣿⣿⡏⠄⠄⠄⠄⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠿⠿⠿⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⢀⠤⠒⣲⡖⠠⣄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿\n" +
                               "⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⢰⠁⢠⡾⠃⢻⡄⠈⢣⠄⠄⠄⠄⠄⠄⣿⣿⣿\n" +
                               "⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠘⣴⠏⠹⣦⠞⢻⣄⡜⠄⠄⠄⠄⠄⠄⢸⣿⣿\n" +
                               "⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠈⠓⠢⠤⠤⠖⠋⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿\n" +
                               "⡟⣡⣦⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⣿\n" +
                               "⠄⣿⣿⣿⠇⠄⣴⣶⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠄⢠⣤⣾⣦⠘\n" +
                               "⡄⠻⣿⡿⠄⢠⣿⣿⠛⣉⠻⣿⣿⣿⣿⣿⣿⡟⠛⢻⣿⡇⠄⢸⣿⣿⣿ \n" +
                               "⣿⣷⣤⣅⢀⢸⣿⣿⣾⣿⣾⣿⣏⠁⣙⣿⣿⣄⠄⣠⣿⣷⠄⠸⣿⠿⢋⣼\n" +
                               "⣿⣿⣿⣿⣿⣆⡹⢿⣿⣿⣿⣄⠈⠉⠉⢡⣿⣿⣿⣿⣿⠟⢀⣰⣶⣾⣿⣿\n" +
                               "⣿⣿⣿⣿⣿⣿⣿⡦⠉⠙⠛⠿⠷⠶⠾⠿⠿⠿⠟⠛⠁⣼⣴⡌⢻⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⠟⣛⡋⠄⠄⠄⠄⠄⢉⠁⣀⠄⠁⠄⠄⢀⣀⣉⣭⣤⣾⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⡃⣾⡿⢂⠄⠄⠄⠄⣩⢓⢉⢃⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⣷⣤⣴⣿⠄⠄⠄⠄⠸⠙⠽⠝⠄⠄⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣖⠒⠒⣲⣶⣶⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
                               "⣿⣿⣿⣿⣿⣿⣿⣿⣇⠾⠿⠿⢋⣸⣄⠻⠿⠿⣂⣽⣿⣿⣿⣿⣿⣿⣿⣿\n")

        @client.command()
        async def 確診(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranConfirm = math.floor(random.random() * 99) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 的武漢肺炎確診機率是: " +
                               str(ranConfirm) + ' %！')

        @client.command()
        async def 點馬(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranFlyHorse = math.floor(random.random() * 90) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 點馬層數: " +
                               str(ranFlyHorse) + " 層！")

        @client.command()
        async def 掉寶(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranTreasure = math.floor(random.random() * 999) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今日掉寶率: " +
                               str(ranTreasure / 10) + " ‰！")

        @client.command()
        async def 一夜致富(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranRich = math.floor(random.random() * 99) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今日就發財機率: " +
                               str(ranRich) + " %！")

        @client.command()
        async def 發財(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                ranRich = math.floor(random.random() * 99) + 1
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 今日就發財機率: " +
                               str(ranRich) + " %！")

        @client.command()
        async def 淨化(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                await ctx.send("淨化時間 : \n" + cleanText)

        @client.command()
        async def 報時(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                timeZone = timezone(timedelta(hours=+8))
                dateTime = str(
                    datetime.now(timeZone).isoformat(timespec="seconds"))
                editDateTime = dateTime.replace("T", " ")
                await ctx.channel.send("目前時間：" + editDateTime[:19])

        @client.command()
        async def 加油(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                await ctx.send("<@" + sender + "> 買車C300 加油加300")

        @client.command()
        async def 大樂透(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                first = random.randint(1, 49)
                biglottery = []
                lotteryStr = ""
                appendorNot = True
                biglottery.append(first)
                while (len(biglottery) < 6):
                    r = random.randint(1, 49)
                    for i in biglottery:
                        if (r == i):
                            appendorNot = False
                            break
                        else:
                            appendorNot = True
                            continue
                    if (appendorNot):
                        biglottery.append(r)
                biglottery = sorted(biglottery)
                for i in range(len(biglottery)):
                    lotteryStr += str(biglottery[i]) + " "
                await ctx.channel.send("<@" + sender + "> 大樂透電腦隨機選號：" +
                                       lotteryStr)

        @client.command()
        async def 威力彩(ctx):
            if (ctx.channel.id == settingDictionary["OfficialChannelID"]):
                sender = str(ctx.author.id)
                first = random.randint(1, 38)
                second = random.randint(1, 8)
                biglottery = []
                lotteryStr = ""
                appendorNot = True
                biglottery.append(first)
                while (len(biglottery) < 6):
                    r = random.randint(1, 38)
                    for i in biglottery:
                        if (r == i):
                            appendorNot = False
                            break
                        else:
                            appendorNot = True
                            continue
                    if (appendorNot):
                        biglottery.append(r)
                biglottery = sorted(biglottery)
                for i in range(len(biglottery)):
                    lotteryStr += str(biglottery[i]) + " "
                await ctx.channel.send("<@" + sender + "> 威力彩第一區號碼：" +
                                       lotteryStr + " 第二區號碼：" +
                                       str(second))

        # @client.command()
        # async def test(ctx, arg):
        #     await ctx.send(arg)

        @client.event  # 調用 event 函式庫
        async def on_ready():  # 當機器人完成啟動時
            print("目前登入身份：", client.user)

        @client.event  # 當有訊息時
        async def on_message(message):

            await client.process_commands(message)
            # region messageEvent

            # 更改日期
            if message.channel.id == settingDictionary["TimerChannelID"]:
                if message.author == client.user:
                    return  # 排除自己的訊息，避免陷入無限循環
                timeZone = timezone(timedelta(hours=+8))
                dateTime = str(datetime.now(
                    timeZone).isoformat(timespec="seconds"))
                timeChannel = client.get_channel(
                    settingDictionary["ClockChannelID"])
                changeName = dateTime[:10] + " 人數 : " + \
                    str(message.guild.member_count)
                await timeChannel.edit(name=changeName)

            else:
                return
            # endregion

        # endregion
