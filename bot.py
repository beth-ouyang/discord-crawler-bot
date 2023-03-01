from discord.ext import commands 
import discord
import json
from crawler import main as ad_crawler

with open('items.json', "r", encoding = "utf8") as file:
    data = json.load(file)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) > 1:
        await message.channel.send(tmp[1])
        print(tmp[1])
    elif message.content == "!申":
       admission_report = ad_crawler()
       await message.channel.send(admission_report)
       print(admission_report)

client.run(data['token'])