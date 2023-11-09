import os, time
from dotenv import load_dotenv
from keep_alive import keep_alive

try:
    import discum
except:
    os.system("pip install git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
    import discum

from discum.utils.slash import SlashCommander

load_dotenv()
TOKEN = os.getenv('TOKEN')
BOT_ID = os.getenv('BOT_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')

bot = discum.Client(token=TOKEN, log=False)

slashsCmd = bot.getSlashCommands(BOT_ID).json()
s = SlashCommander(slashsCmd)
data = s.get(['bump'])

while True:
    print("Online.")
    bot.triggerSlashCommand(BOT_ID, CHANNEL_ID, GUILD_ID, data)
    time.sleep(7200)
    keep_alive()
    bot.gateway.run(auto_reconnect=True)