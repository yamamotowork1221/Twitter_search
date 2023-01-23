import tweepy
from app import tweepy_authentication
from flask import session

# ツイート取得
def search_results():


    client = tweepy_authentication.authentication() # 認証
    tweets = client.search_recent_tweets(query = session['input_keyword'] ,  # 検索ワード
                                         max_results = 20,  # 取得件数
                                         user_fields = 'profile_image_url',  # プロフィール画像 URL
                                         tweet_fields = ['author_id', 'created_at', 'public_metrics'] , # 投稿者ID 投稿日時 いいね 
                                         expansions = ['author_id']
                                         )

    if tweets.data is not None:
        for (tweet,user) in zip(tweets[0],tweets.includes['users']):
            print(user.name + "@" + user.username)
            print(tweet.text)
            print()
    else:
        print('該当なし')
        return None
    return tweets[0],tweets.includes['users']
    
    client = tweepy_authentication.authentication() # 認証
    tweets = client.search_recent_tweets(query = session['input_keyword'] ,  # 検索ワード
                                         max_results = 20,  # 取得件数
                                         user_fields = 'profile_image_url',  # プロフィール画像 URL
                                         tweet_fields = ['author_id', 'created_at', 'public_metrics'] , # 投稿者ID 投稿日時 いいね 
                                         expansions = ['author_id']
                                         )

    if tweets.data is not None:
        for (tweet,user) in zip(tweets[0],tweets.includes['users']):
            print(user.name + "@" + user.username)
            print(tweet.text)
            print()
    else:
        print('該当なし')
        return None
    return tweets[0],tweets.includes['users']