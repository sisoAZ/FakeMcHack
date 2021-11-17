import discord
import os

from util import sort_args

import mergeText
import mergeOverlay

os.makedirs(os.getcwd() + "/files", exist_ok=True)
DIR = os.getcwd() + "/files/"

client = discord.Client()

@client.event
async def on_ready():
    print("Discord Logged in " + client.user.name)

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    args = sort_args(message.content)
    if args[0] != "-fakechat" and args[0] != "-fakehack":
        return
    #返信じゃなかったら
    if message.reference == None:
        if len(message.attachments) < 1:
            await message.channel.send("Usage: `-fakechat (text)` and image file")
            await message.channel.send("Usage: `-fakehack (wurst|pvp|vape)` and image file")
            return
    if message.reference != None:
        replyMessage = await message.channel.fetch_message(message.reference.message_id)
    if args[0] == "-fakechat":
        if len(args) < 2:
            await message.channel.send("`Please enter text`")
            return
    if args[0] == "-fakehack":
        if len(args) < 2:
            await message.channel.send("`Please enter type (wurst|pvp|vape)`")
            return
        elif not any(["wurst", "pvp", "vape"]):
            await message.channel.send("`Please enter type (wurst|pvp|vape)`")
            return
    if message.reference == None:
        file = message.attachments[0]
    else:
        file = replyMessage.attachments[0]
    filename = file.filename
    extension = os.path.splitext(filename)[1]
    if extension != ".png" and extension != ".jpg":
        await message.channel.send("Please file extension is .jpg or .png")
        return
    attachmentFilePath = DIR + filename
    await file.save(attachmentFilePath)
    
    if args[0] == "-fakechat":
        chat = message.content.split(" ", 1)[1]
        imagePath = mergeText.drawText(attachmentFilePath, chat.split(","))
        await message.channel.send(file=discord.File(imagePath))
        os.remove(imagePath)
        os.remove(attachmentFilePath)
    
    if args[0] == "-fakehack":
        if args[1] == "wurst":
            filename = "wurst.png"
        elif args[1] == "pvp":
            filename = "other.png"
        elif args[1] == "vape":
            filename = "vape.png"
        guiPath = os.getcwd() + "/hackgui/" + filename
        imagePath = mergeOverlay.margeGui(attachmentFilePath, guiPath)
        await message.channel.send(file=discord.File(imagePath))
        os.remove(imagePath)
        os.remove(attachmentFilePath)

client.run("")
