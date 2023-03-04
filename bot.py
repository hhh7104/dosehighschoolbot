import discord
from discord.ext import commands

client = commands.Bot(command_prefix="/")

banned_list = []
info_list = {}

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def 출입금지(ctx, name: str):
    banned_list.append(name)
    await ctx.send(f"{name}님을 출입금지 목록에 추가했습니다.")

@client.command()
async def 출입금지해제(ctx, name: str):
    if name in banned_list:
        banned_list.remove(name)
        await ctx.send(f"{name}님을 출입금지 목록에서 해제했습니다.")
    else:
        await ctx.send(f"{name}님은 출입금지 목록에 없습니다.")

@client.command()
async def 출입금지목록(ctx):
    if len(banned_list) == 0:
        await ctx.send("출입금지 목록이 비어있습니다.")
    else:
        banned_list_str = "\n".join([f"{i+1}. {name}" for i, name in enumerate(banned_list)])
        await ctx.send(f"출입금지 목록:\n{banned_list_str}")

@client.command()
async def 정보변경(ctx, name: str, position: str):
    if name in info_list:
        info_list[name].append(position)
    else:
        info_list[name] = [position]
    await ctx.send(f"{name}님의 정보를 변경했습니다.")

@client.command()
async def 정보확인(ctx, name: str):
    if name in info_list:
        positions_str = "\n".join([f"{i+1}. {position}" for i, position in enumerate(info_list[name][:-1])])
        message = f"{name}님의 정보 변경 기록:\n{positions_str}\n\n현재 {name}님은 {info_list[name][-1]}입니다."
        await ctx.send(message)
    else:
        await ctx.send(f"{name}님의 정보가 없습니다.")


client.run("MTA4MTIwODAzNTk2MTIxNzA4NA.GxysUj.S3mLmY11FBuN-s10ofRqqQsGrz3cF_wxUwdu9Y")