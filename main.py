# env
import os
from dotenv import load_dotenv
load_dotenv()
UID = 405582582
import fsq, places

from telethon import TelegramClient, events

bot = TelegramClient('bot', int(os.environ['TGAID']), os.environ['TGAHASH']).start(bot_token=os.environ['TWARM'])

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
	await event.respond('Twarm is a Telegram - Swarm bot.')
	raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
	if event.peer_id.user_id != UID:
		await event.respond("**你无权查看**")
		return
	t = event.text
	print(t)
	if t.find("foursquare.com/v/") != -1:
		name = t.split(" - ")[0]
		vid = t.split('/')[-1]
		res = places.record(vid, name)
		await event.respond(f"`venueId` 为 `{vid}` 的 **{name}** 已加入数据库，数据项 ID 为 {str(res)} 。")

resp = {}

@bot.on(events.NewMessage(pattern='/add'))
async def add(event):
	if event.peer_id.user_id != UID:
		# await event.respond("**你无权查看**")
		return
	print(event)
	paras = event.text.split(" ")
	if len(paras) >= 3:
		paras[1] = paras[1].replace("`", '')
		recds = places.lookup(paras[1])
		print("recds:")
		print(recds)
		print("  ")
		if recds is not []:
			paras[1] = recds[0]["v"]
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