import os                                                               
import socket                                                           
import json                                                             
import time                                                             
import random
import facebook
import tweepy
                                                                        
HOST = "127.0.0.1"                                                      
PORT = 4089                                                            
INTERVAL = 60                                                           
               

def main_facebook(msg):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "642153615917075",  # Step 1
    "access_token" : "CAAL5CfdWRIEBAHodHWlY78Ldq8QoYC5wEYDtZC2oOinzFQMqmZAgKk4hZAcJXivA0oR5mrIfZCD5rcbBdofZBGl0Mjv7d0ZAcJ6ZAL83ZCrmPk155B5Xv66JcfSG5jxHTCfOLF36PE6e0VMWmZBZCA4OK48e91ByKCdHLZCeJ53vSRaLQT9wxST3wVIq2O97jCkX98QlfsDoelS8VCtCl5F87b9"   # Step 3
    }

  api = get_api_facebook(cfg)
  status = api.put_wall_post(msg)

def get_api_facebook(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

def get_api_twitter(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main_twitter(tweet):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "IIn0cIWGd80iBSN9EMnZhPmnP",
    "consumer_secret"     : "AslJfJM8iN0jx9uKUQD6YOGi5vwMnLcKof60gvJQBpi8f6lTA7",
    "access_token"        : "3148684387-Oqw2LPcaCJhcu1OMTriSHFv0FwOUXqEjK4d2e1T",
    "access_token_secret" : "D4eHHBAUtfyX3IvlmMuH198w0p03TwV09gkKlDwb2muzH"
    }

  api = get_api_twitter(cfg)
  status = api.update_status(status=tweet)

def register_metric(metric_name, metric_type):                          
    msg = {                                                             
        "n": metric_name,                                               
        "t": metric_type                                               
    }                                                         
                                                           
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(msg), (HOST, PORT))             
                                              
                                                           
def send_data(metric_name, value):                         
    msg = {                                                
        "n": metric_name,                     
        "v": value                                         
    }                                                      
                                                           
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(msg), (HOST, PORT)) 

def get_temp():                                                         
    temp = random.randrange(28,40,1)                                                          
    temp_src = "/sys/class/thermal/thermal_zone0/temp"                  
                                                                        
    #if os.path.isfile(temp_src):                                        
    #    try:                                                            
    #        f = open(temp_src)                                          
    #        t = f.read()                                               
    #        temp = int(float(t)) / 1000                       
    #    except IOError:                                    
    #        pass                                           
                                                           
    return temp                                            

def get_presion():
    presi = random.randrange(0,220,1)
    return presi

                                                           
next_send_time = 0                                         
while True:                                                
    t = time.time()                                        
    if t > next_send_time:                                 
        temp = get_temp()                                  
        pres = get_presion() 
        msg = ""

        if pres < 60:
           msg = "Bradicardia"
        elif pres > 100 and pres < 120 and temp >= 35 and temp <= 37: 
           msg = "Taquicardia"
        elif pres > 120 or temp > 37: 
           msg = "Taquicardia (Modo correr)"
        elif pres>= 60 and pres <= 100 and temp > 37:
            msg = "Temperatura alta" 

        main_facebook(msg)
        main_twitter(msg)
        send_data("presion", pres)                
        send_data("temperature", temp)                
        print(temp)
        print(pres)                                      
        next_send_time = t + INTERVAL                      
    time.sleep(10)
