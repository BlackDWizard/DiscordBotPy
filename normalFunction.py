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

commandBoolean = ""

# region bot action


class normalFunction(commands.Cog):
    def __init__(self, client):

        @client.command()
        async def 乳滑(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                await ctx.send(
                    "https://tenor.com/view/miss-you-we-miss-them-gif-13362284")
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def 沒過(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                await ctx.send(file=discord.File('./image/boom.jpg'))
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def 過了(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                await ctx.send(file=discord.File('./image/pass.gif'))
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def PA(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                await ctx.send(
                    "https://tenor.com/view/worship-pa-pearl-abyss-gif-20263613")
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def 大便(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                ranPopo = math.floor(random.random() * 50) + 1
                await ctx.send("<@" + str(ctx.author.id) + "> 今天大便最長能拉到 " +
                               str(ranPopo) + " 公分！")
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def 尻尻(ctx):
            if (ctx.channel.id == settingDictionary["DebugChannelID"]):
                ranKaokao = math.floor(random.random() * 60) + 1
                await ctx.send("<@" + str(ctx.author.id) + "> 今天尻尻最久能尻 " +
                               str(ranKaokao) + " 分鐘！")
                global commandBoolean
                commandBoolean = "t"

        @client.command()
        async def test(ctx, arg):
            await ctx.send(arg)
            global commandBoolean
            commandBoolean = "t"

        @client.event  # 調用 event 函式庫
        async def on_ready():  # 當機器人完成啟動時
            print("目前登入身份：", client.user)

        @client.event  # 當有訊息時
        async def on_message(message):

            await client.process_commands(message)
            global commandBoolean

            sender = str(message.author.id)
            random.seed()
            ranDice = math.floor(random.random() * 1000000) + 1
            ranBdo = math.floor(random.random() * 99) + 1
            ranDick = math.floor(random.random() * 30) + 1
            ranConfirm = math.floor(random.random() * 99) + 1
            ranRich = math.floor(random.random() * 99) + 1
            ranFlyHorse = math.floor(random.random() * 90) + 1
            ranTreasure = math.floor(random.random() * 999) + 1
            # ranMemberTag = math.floor(random.random() * 3)
            ranFood = math.floor(random.random() * len(food))
            cmdList = ""
            # tagLoopStart=""

            # if "恩" in message.content or "嗯" in message.content or "ㄣ" in message.content or "煾" in message.content or "蒽" in message.content or "慁" in message.content or "摁" in message.content:
            #     if "克羅恩" in message.content:
            #         return
            #     else:
            #         await message.delete()

            # region messageEvent
            if message.channel.id == settingDictionary["DebugChannelID"]:

                if "@" in message.content:
                    await client.get_channel(866942351604056065).send(
                        message.author.name + " : " + message.content[22:])
                else:
                    await client.get_channel(866942351604056065).send(
                        message.author.name + " : " + message.content)

                if message.author == client.user:
                    return  # 排除自己的訊息，避免陷入無限循環

                if commandBoolean == "t":
                    commandBoolean = ""
                    return

                if message.content == "ping":
                    await message.channel.send("pong")  # 如果包含 ping，機器人回傳 pong

                if (message.content[:1] == "~"):  # cmd part 機器人指令測試

                    cmd = message.content[1:]
                    if message.author == client.user:
                        return  # 排除自己的訊息，避免陷入無限循環

                    if cmd == cmdArray[0]:
                        await message.channel.send("吃" + food[ranFood] + "吧~~")
                    elif cmd == cmdArray[1]:
                        await message.channel.send("<@" + sender + "> 骰出了 " +
                                                   str(ranDice) + " 點！")

                    elif cmd == cmdArray[2]:
                        await message.channel.send("<@" + sender + "> 今天衝裝機率: " +
                                                   str(ranBdo) + " %！")

                    elif cmd == cmdArray[3]:
                        await message.channel.send("<@" + sender + ">, 你又沒對象在69尛")

                    elif cmd == cmdArray[4]:
                        await message.channel.send("誰再雞腿bang當 群主就讓他媽媽復活")

                    elif cmd == cmdArray[5]:
                        await message.channel.send("<@" + sender + "> 今天雞雞最長能硬到 " +
                                                   str(ranDick) + " 公分！")

                    elif cmd == cmdArray[6]:
                        await message.channel.send("```" + "Server name:" +
                                                   message.guild.name +
                                                   "\nTotal members:" +
                                                   str(message.guild.member_count) +
                                                   "```")

                    elif cmd == cmdArray[7]:
                        await message.channel.send("早安啊~" + "<@" + sender +
                                                   "> 今天也要繼續努力唷~")

                    elif cmd == cmdArray[8]:
                        await message.channel.send("午安啊~" + "<@" + sender +
                                                   "> 吃飽了嗎？要堅持住唷~")

                    elif cmd == cmdArray[9]:
                        await message.channel.send("晚安啊~" + "<@" + sender +
                                                   "> 你好嗎？你今天過得好嗎？")

                    elif cmd == cmdArray[10]:
                        await message.channel.send("⣿⣿⣿⣿⡏⠄⠄⠄⠄⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠿⠿⠿⣿⣿⣿\n" +
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

                    # elif cmd == cmdArray[11]:
                    #     await client.get_channel(733373303535960085).send("<@" + memberTagArray[ranMemberTag] + ">")
                    #     ranMemberTag = Math.floor(Math.random() * 3);
                    #     tagLoopStart = setInterval(function() {tagLoop()}, 10000)

                    # elif cmd == cmdArray[12]:
                    #     clearInterval(tagLoopStart);

                    elif cmd == cmdArray[13]:
                        await message.channel.send("<@" + sender + "> 的武漢肺炎確診機率是: " +
                                                   str(ranConfirm) + ' %！')

                    elif cmd == cmdArray[14]:
                        await message.channel.send("<@" + sender + "> 點馬層數: " +
                                                   str(ranFlyHorse) + " 層！")

                    elif cmd == cmdArray[15]:
                        await message.channel.send("<@" + sender + "> 今日掉寶率: " +
                                                   str(ranTreasure / 10) + " ‰！")

                    elif cmd == cmdArray[16]:
                        await message.channel.send("<@" + sender + "> 今日就發財機率: " +
                                                   str(ranRich) + " %！")
                    elif cmd == cmdArray[17]:
                        await message.channel.send("<@" + sender + "> 今日就發財機率: " +
                                                   str(ranRich) + " %！")

                    elif cmd == cmdArray[18]:
                        await message.channel.send("淨化時間 : \n" + cleanText)

                    elif cmd == cmdArray[19]:
                        timeZone = timezone(timedelta(hours=+8))
                        dateTime = str(
                            datetime.now(timeZone).isoformat(timespec="seconds"))
                        editDateTime = dateTime.replace("T", " ")
                        await message.channel.send("目前時間：" + editDateTime[:19])
                    elif cmd == cmdArray[20]:
                        await message.channel.send("<@" + sender + "> 買車C300 加油加300")
                    elif cmd == cmdArray[21]:
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
                        await message.channel.send("<@" + sender + "> 大樂透電腦隨機選號：" +
                                                   lotteryStr)
                    elif cmd == cmdArray[22]:
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
                        await message.channel.send("<@" + sender + "> 威力彩第一區號碼：" +
                                                   lotteryStr + " 第二區號碼：" +
                                                   str(second))

                    elif cmd == "指令":
                        for cmd in cmdArray:
                            cmdList = cmdList + "~" + cmd + "\n"
                        await message.channel.send("```\n目前有這些指令：\n" + cmdList + "```")
                        cmdList = ""
                    else:
                        await message.channel.send("還沒想出來的指令= = bydebug")
                else:
                    return

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
