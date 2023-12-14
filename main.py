import discord
import random   

def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)
    return sifre

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "Yazı Çıktı :)"
    else:
        return "Tura Çıktı :)"
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$name'):
        await message.channel.send("My Name Is Bot Slime!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye!")    
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$pass'):
        await message.channel.send(sifre_olusturucu(10))
    elif message.content.startswith('$'):
        await message.channel.send("Bu komutu anlayamadım :(")

client.run("MTE4MDIxMTM2OTYwNjM5Nzk3Mw.Gu5y3k.bhYUSx5CcbUYr2rKotEM02Y6TVx2YZXsXk686E")