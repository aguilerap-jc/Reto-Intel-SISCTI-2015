import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "IIn0cIWGd80iBSN9EMnZhPmnP",
    "consumer_secret"     : "AslJfJM8iN0jx9uKUQD6YOGi5vwMnLcKof60gvJQBpi8f6lTA7",
    "access_token"        : "3148684387-Oqw2LPcaCJhcu1OMTriSHFv0FwOUXqEjK4d2e1T",
    "access_token_secret" : "D4eHHBAUtfyX3IvlmMuH198w0p03TwV09gkKlDwb2muzH"
    }

  api = get_api(cfg)
  tweet = "Hellow, world!"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
