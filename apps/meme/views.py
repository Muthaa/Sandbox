import os
from flask import Blueprint, render_template
from apps.meme import blueprint
import requests
import json
from jinja2 import TemplateNotFound

def get_memes():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_preview = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_preview, subreddit

@blueprint.route('/')
def index():
    meme_pic, subreddit = get_memes()
    return render_template("memes.html", meme_pic=meme_pic, subreddit=subreddit)
