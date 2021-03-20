import foursquare
# env
import os
from dotenv import load_dotenv
load_dotenv()

client = foursquare.Foursquare(client_id=os.environ['ID_4SQ'], client_secret=os.environ['SEC_4SQ'], redirect_uri=os.environ['REDIR_4SQ'])
# auth_uri = client.oauth.auth_url()
client.set_access_token(os.environ['ACC_4SQ'])

def add(venueId: str, shout: str, private: bool = False, tweet: bool = False):
	res = client.checkins.add(
		params={
			"venueId": venueId,
			"shout": shout + " (Checked in via Twarm, a Telegram-Swarm bot.)",
			"broadcast": "public"
			}
	)
	return res