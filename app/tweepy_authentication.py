import tweepy
import os
from dotenv import load_dotenv

def authentication():
    # .envファイルの内容を読み込見込む
    load_dotenv()

    # 認証　
    client = tweepy.Client(
        consumer_key = os.environ['api_key'],
        consumer_secret = os.environ['api_key_secret'],
        access_token = os.environ['access_token'],
        access_token_secret = os.environ['access_token_secret'],
        bearer_token = os.environ['bearer_token']
    )
    
    return client