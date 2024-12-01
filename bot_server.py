from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Replace 'your-token-here' with your bot's token
TOKEN = '7340560560:AAHagBxyC66g0xU9Tk7sc00ZQZ0QjXTjeIs'

# Set the webhook URL (replace this with your ngrok URL)
WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://3185-2a06-c701-78d6-c700-1cfb-5fd8-8bd2-19a0.ngrok-free.app/message'

requests.get(WEBHOOK_URL)  # Set the webhook

@app.route('/sanity')
def sanity():
    return "Server is running"

@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")

    # Get the chat ID and message text from the incoming request
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    # Respond to the user with the same text they sent
    response_text = f"You said: {text}"
    send_message(chat_id, response_text)

    # Send a "Got it" message as well
    send_message(chat_id, "Got it")

    return Response("success")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(port=5002)
