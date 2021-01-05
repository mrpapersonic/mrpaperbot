import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!!')
@client.event

async def on_ready():
	print("I am ready!")

@client.command()
async def sub(ctx):
	await ctx.channel.send("https://www.youtube.com/channel/UCsEF9mQtJiPAjW3FQDUzbGw?sub_confirmation=1")

@client.command()
async def kill(ctx):
	await ctx.channel.send("kill yourself")

@client.command()
async def unsub(ctx):
	await ctx.channel.send("from dantdm")

@client.command()
async def giveexmodback(ctx):
	await ctx.channel.send("hes getting it back in like a few days jeez")

@client.command()
async def itstime(ctx):
	await ctx.channel.send("to give ex-mods back to misspapsus")

@client.command()
async def stop(ctx):
	await ctx.channel.send("`@everyone` STOPPPP")

@client.command()
async def fart(ctx):
	await ctx.channel.send("you smell")

@client.command()
async def what(ctx):
	await ctx.channel.send("https://i.imgur.com/5dgrsL4.png")

@client.command()
async def howoldareyou(ctx):
	await ctx.channel.send("3")

@client.command()
async def succ(ctx):
	await ctx.channel.send("https://i.imgur.com/vV2C7Km.png copyright creeft's spicy memes *all* ***lefts*** *reserved*")

@client.command()
async def bandicam(ctx):
	await ctx.channel.send("https://www.youtube.com/watch?v=UiRBPZP02Cs")

@client.command()
async def duckonscreen(ctx):
	await ctx.channel.send("https://i.imgur.com/U0xUi3l.png")

@client.command()
async def duckscreendownload(ctx):
	await ctx.channel.send("https://i.imgur.com/OHbQ7xh.png")

@client.command()
async def alphysismywaifu(ctx):
	await ctx.channel.send("https://i.imgur.com/RfV9Y3J.jpg")

@client.command()
async def lenny(ctx):
	await ctx.channel.send("( ͡° ͜ʖ ͡°)")

@client.command()
async def roblox(ctx):
	await ctx.channel.send("`@everyone` dont buy robux")

@client.command()
async def roblox(ctx):
	await ctx.channel.send("`@everyone` wear your seatbelt")

@client.command()
async def technoblade(ctx):
	await ctx.channel.send("https://www.youtube.com/user/technothepig?sub_confirmation=1")

@client.command()
async def didyoudie(ctx):
	await ctx.channel.send("`@everyone` did you die?")

@client.command()
async def ididdie(ctx):
	await ctx.channel.send("m'kay")

@client.command()
async def ididntdie(ctx):
	await ctx.channel.send("https://i.imgur.com/sR0CSGQ.jpg")

@client.command()
async def downloadcoder(ctx):
	await ctx.channel.send("https://code.visualstudio.com/Download")

@client.command()
async def nope(ctx):
	await ctx.channel.send("https://cdn.drawception.com/images/panels/2015/3-23/BC322qXPhz-4.png")

@client.command()
async def monkeysee(ctx):
	await ctx.channel.send("monkey do")

@client.command()
async def creeft(ctx):
	await ctx.channel.send("UNBAN CREEFT")

@client.command()
async def pack(ctx):
	await ctx.channel.send("pack: http://www.mediafire.com/file/2w0kbab06250sdp/%21++++++++++++++++++++++++Paper%27s+Mashup+%28EXTRACT%29.zip")

@client.command()
async def share(ctx):
	await ctx.channel.send("http://bit.ly/MrPaperBot")

#wtf is this
@client.command()
async def spam(ctx):
	await ctx.channel.send(".               hi")

@client.command()
async def masturbation(ctx):
	await ctx.channel.send("https://i.imgur.com/snRiv5d.png copyright creeft's spicy memes **all** ***lefts*** **reserved**")

@client.command()
async def nub(ctx):
	await ctx.channel.send("i am a complete nub [yes its a joke]")

#not possible in discord.py
#nevermind
async def on_message(message):
	await client.process_commands(message)
	if "driver - the eye of truth" in message.content.lower():
		await Bot.send_message(message.channel, 'yes')
""" commented because fork bomb
    if "a" in message.content.lower():
        await Bot.send_message(message.channel, 'aaaaaaaaaaaaa')
"""
@client.command()
async def soop(ctx):
	await ctx.channel.send("http://decameron.org/wp-content/uploads/2013/05/SooP2.Logo1_.5.jpg")


client.login("token");
