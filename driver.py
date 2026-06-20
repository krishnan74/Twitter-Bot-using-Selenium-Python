import twitterbot as tb
from dotenv import load_dotenv
load_dotenv()
import os

import time
import uuid
from pymongo import MongoClient
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__)
bot = None

client = MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING"))

@app.route('/getTrendingTopics', methods=['GET'])
def get_trending_topics():
    database = client.get_database("topics")
    topicsCollection = database.get_collection("trendingTopics")

    
    global bot
    if not bot:
        bot = tb.Twitterbot("rdk07042004@gmail.com", "krishnanoo7")
        bot.login()
        time.sleep(5)
    result = bot.getTrendingTopics()

    # document = {
    #     "id": str(uuid.uuid4()),
    #     "topics": result
    # }
    return jsonify({result})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
