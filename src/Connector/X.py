import tweepy

class X:
    
    def __init__(self, apiKey, apiSecret, accessToken, accessSecret):
        
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.accessToken = accessToken
        self.accessSecret = accessSecret
        self.api = None
    
    def setApi(self, api):
        
        self.api = api
        return self.api
        
    def connect(self):
        
        auth = tweepy.OAuthHandler(self.apiKey, self.apiSecret)
        auth.set_access_token(self.accessToken, self.accessSecret)
        self.api = self.setApi(tweepy.API(auth))
        
        try:
            self.api.verify_credentials()
            print("Log to X successful")
        except tweepy.TweepError as e:
            print(f"Log to X fail : {e}")
            return False

