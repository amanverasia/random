from twilio.rest import Client
import time
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:'



def send_message(message):
	client.messages.create(body=message,
	                        from_=from_whatsapp_number,
	                        to=to_whatsapp_number)


for x in range(10):
    send_message(f'I Love you! {x+1} times')
    time.sleep(2)