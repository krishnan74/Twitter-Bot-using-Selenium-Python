import twitterbot as tb
import secrets
import time
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__)
bot = None

@app.route('/getTrendingTopics', methods=['GET'])
def get_trending_topics():
    global bot
    if not bot:
        bot = tb.Twitterbot("rdk07042004@gmail.com", "krishnanoo7")
        bot.login()
        time.sleep(5)
    result = bot.getTrendingTopics()
    return jsonify({"topics": result})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
