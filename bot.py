from dotenv import load_dotenv
import os
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from hazm import *
n = Normalizer()
load_dotenv()
Bot = Client(
    "PersianT2SBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
c = ["g++", "-Wall", "kasre_ezafeh.cpp", "hazm.cpp", "hazm.h", "-o", "ezafeh"]
#os.system('python3-config --ldflags --embed')
compile_process = subprocess.run(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if compile_process.returncode == 0: 
    print("Compilation successful.")
else:
    print("Compilation failed.") 
    print(compile_process.stderr.decode())


START_TXT = """
Hi {}, I'm Persian TTS Bot.

Just send me your text.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/soebb'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
)


@Bot.on_message(filters.private & filters.text)
async def t2s(bot, m):
    input = m.text
    run_process = subprocess.run("./ezafeh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input, encoding='ascii')
    error = run_process.stderr.decode()
    print(error)
    out = run_process.stdout.decode()
    msg = await m.reply(out)


Bot.run()
