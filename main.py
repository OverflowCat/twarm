# env
import os
from dotenv import load_dotenv
load_dotenv()

import fsq

from telethon import TelegramClient, events

bot = TelegramClient('bot', int(os.environ['TGAID']), os.environ['TGAHASH']).start(bot_token=os.environ['TWARM'])

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
	print(event)
	await event.respond('Twarm is a Telegram - Swarm bot.')
	raise events.StopPropagation
'''
@bot.on(events.NewMessage)
async def echo(event):
	await event.respond(event.text)
'''
resp = {}

@bot.on(events.NewMessage(pattern='/add'))
async def add(event):
	print(event)
	paras = event.text.split(" ")
	if len(paras) >= 3:
		paras[1] = paras[1].replace("`", '')
		print(paras)
		resp = fsq.add(paras[1], paras[2])
		print(resp)
		url = resp["checkin"]["checkinShortUrl"]
		await event.respond(url)
	else:
		await event.respond("Please SHOUT!")

def main():
	"""Start the bot."""
	bot.run_until_disconnected()

if __name__ == '__main__':
	main()