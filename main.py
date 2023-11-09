import os, time
from dotenv import load_dotenv
from keep_alive import keep_alive
import schedule

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

def bump():
    bot.triggerSlashCommand(BOT_ID, CHANNEL_ID, GUILD_ID, data)
    print("Bumped!")

schedule.every(10).minutes.do(bump)

keep_alive()
while True:
    schedule.run_pending()
    time.sleep(1)