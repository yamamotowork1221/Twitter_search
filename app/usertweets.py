import tweepy
from app import tweepy_authentication
from flask import session

# ツイート取得
def usertweets():
    client = tweepy_authentication.authentication() # 認証
    user_data = client.get_user(username = session['input_keyword']) # username → user id
    user_id = user_data.data.id
    time_line = client.get_users_tweets(id = user_id,
                                        max_results = 20
                                        )
    tweets = time_line

    print(user_data)
    
    if tweets is not None:
        for tweet in tweets[0]:
            print(tweet.text)
            print()
    else:
        print('該当なし')
        return None
    return tweets[0],user_data[0]