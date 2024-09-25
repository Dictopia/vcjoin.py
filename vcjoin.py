import time
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from secfix import sectotime

load_dotenv()
vcJoinedTime = {} #ユーザの入室したUNIX時間を一時的に保存する辞書

print(f"""
vcjoin ver 0.1
    launching...
-----------------------------
""")

boot_time = time.perf_counter()

intents = discord.Intents.all()
intents.typing = False
bot = commands.Bot(intents=intents, command_prefix=os.getenv('BOT_PREFIX'))

@bot.event
async def on_ready():
    print(f"Connected to API in {round(time.perf_counter() - boot_time, 2)}s!\nConsole logged in as : {bot.user}")

@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    await ctx.send(f"[vc-join]Pong! Current latency is {ping}ms.")


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        messageChID = bot.get_channel(int(os.getenv('VC_MESSAGE_CHANNEL')))
        targetChIDs = [int(os.getenv('VC_TARGET_CHANNEL_1')), int(os.getenv('VC_TARGET_CHANNEL_2'))]
        #退出通知
        if before.channel is not None and before.channel.id in targetChIDs:
            spenttime = int(time.time() - vcJoinedTime[f"{member.id}"]) #ユーザーがVCにいた時間
            if member.id != int(os.getenv('IGNORE_ID')):
                await messageChID.send(f"{before.channel.name} | **{member.name}** left ({sectotime(spenttime)})")
        #入室通知
        if after.channel is not None and after.channel.id in targetChIDs:
            if member.id != int(os.getenv('IGNORE_ID')):
                await messageChID.send(f"{after.channel.name} | **{member.name}** joined")
            vcJoinedTime[f"{member.id}"] = time.time()



bot.run(os.getenv('BOT_TOKEN'))