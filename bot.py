from discord.ext import commands 
import discord
from crawler import admission_main as ad_crawler
from crawler import line_emoji_download as line_emoji_download

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

    if message.content.startswith('說'):
      tmp = message.content.split("說",2)
      if len(tmp) > 1:
        await message.channel.send(tmp[-1])
        print(tmp[-1])
    elif message.content=='申':
       admission_report = ad_crawler()
       await message.channel.send(admission_report)
       print(admission_report)
    elif message.content.startswith('!line下載>>'):
      tmp = message.content.replace(" ", "").split(">>",2)
      line_emoji_download(tmp[-1])
      await message.channel.send('下載好了!', file=discord.File("line_emoji.zip"))
    elif message.content=='!指令':
      await message.channel.send("""目前有的指令:
      1. 說 + 想講的話 : 說安安 -> return 安安
      2. 下載line貼圖/表情貼 : !line下載>> + line store網址 -> return zip檔
      3. 查看最近米國研究所回報 : 申 -> return 結果
      """)

client.run(os.environ['token'])
