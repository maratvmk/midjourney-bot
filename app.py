from flask import Flask, request
from midjourney import start_bot
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def healthcheck():
    return 'Great'


@app.route('/generate')
def get_query_param():
    art = request.args.get('art')
    topic = request.args.get('topic')
    channel_url = request.args.get('channel')

    if topic and channel_url:
        start_bot(channel_url, topic, art)

    return f"The value of 'query' is: {topic}"


if __name__ == '__main__':
    app.run(debug=True)
