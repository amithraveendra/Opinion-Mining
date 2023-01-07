import tweepy
api_key = "otGBf9gcDR8iS9hBYRZZxeiUv"
api_secret = "IJnJ8wv6v9yhWxx9M30tWYQ8dNcPGvJn4ABTBZ3UyJEqZ8Og5Y"
bearer_token =r"AAAAAAAAAAAAAAAAAAAAADaqkgEAAAAA%2FAqFnknF1nTK%2FWouuR2VXrGscJM%3DeIp4IIF2cPRWMGliYbnHWtO46OI3LbS131mfrpCin0R2iuym2z"
access_token = "1604379731247661056-rppWgrXHwvvOKY4TaQS5kexeEbf8LM"
access_token_secret = "CMprzYhCQqWUAxqGCprBKeIy9SirlvfTFFnmA86HoogC4"
client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)
client.create_tweet(text="")
