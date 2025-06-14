from twilio.rest import Client
import os
from twilio.base.exceptions import TwilioRestException

# Replace these with your Twilio credentials and phone numbers
TWILIO_ACCOUNT_SID = 'AC1298d6329fb1f118754f1f6f3ae74d'  # From Twilio Console
TWILIO_AUTH_TOKEN = 'c549d0134e3d19080ae9ce5677ecad'    # From Twilio Console
TWILIO_PHONE_NUMBER = '+19413520731'          # Your Twilio phone number
RECIPIENT_PHONE_NUMBER = '+923409777222'       # Recipient's phone number

def send_sms(message_body):
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        
        print(f"Message sent successfully! SID: {message.sid}")
        return message.sid
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")
        return None

if __name__ == "__main__":
    # Example message
    message_to_send = "Hello! shezad khna sanga ye ."
    send_sms(message_to_send)