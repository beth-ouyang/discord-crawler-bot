# Discord Crawler Bot

### Usage
Listening to the messages in Discord Channel, and react upon the specific command.

### Commands
#### 1. Echo
- Example:  
`說 Hello World` -> return "Hello World"
#### 2. Download Line stickers/emojis
- Example:  
`!line下載>> + Line store link` -> return zip file containing the sticker images
- [Line store link example](https://store.line.me/stickershop/product/1287660/zh-Hant)
#### 3. Web scrapping for the latest application updates
- Motivation:  
People post the updates of their application for master's program in the forum. By scrapping these posts, we can better estimate which school is sending out the results.

- Example:  
`申` -> return the latest posts regarding to the programs that I applied for.

### Execution on the local machine
1. Set the environment variables: `token`, which can be found in the [Discord Developers Portal](https://discord.com/developers/applications)
2. Simply run the `bot.py` file.

### Deploy on [Render](https://dashboard.render.com/)
1. Add a web service by importing the Github repository
2. Set the build command `pip install -r requirements.txt`
3. Set the start command `python bot.py`
4. Set the environment variables: `token`, which can be found in the [Discord Developers Portal](https://discord.com/developers/applications)
