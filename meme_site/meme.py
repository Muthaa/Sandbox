from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_memes():
	url="https://meme-api.com/gimme"
	response= json.loads(requests.request("GET",url).text)
	meme_preview=response["preview"][-2]
	subreddit=response["subreddit"]
	return meme_preview,subreddit

@app.route('/')
def index():
	meme_pic,subreddit=get_memes()
	return render_template("memes.html",meme_pic=meme_pic,subreddit=subreddit)

app.run(host="127.0.0.1",port=5006, threaded=True,debug=True)
