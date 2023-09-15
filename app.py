from flask import Flask, request
from midjourney import start_bot

app = Flask(__name__)

@app.route('/')
def healthcheck():
    return 'Great'

@app.route('/mid')
def get_query_param():
    query = request.args.get('query')
    if query:
        start_bot('realistic', 'https://discord.com/channels/1149334794837180577/1149334795546009612', query, 'building materials')
    return f"The value of 'query' is: {query}"

if __name__ == '__main__':
    app.run(debug=True)
