import requests
import csv, getpass, json, os, time, urllib
import oauth2 as oauth
consumer_key= 'bkNvGAWGpim9rZMLx1YRSH6CV'
consumer_secret='hu9zUGF3s2shnRz4LF7A4hz79axIYIERtvNCQEPDJfe1pCF4hA'
access_token_key = '117810107-6wyc6jY8Db3B7tAwJHjMCgSoTwFaWIguW5GbXSC2'
access_token_secret = 'F6L2sR8MaqLb5LTG8qj3FzB6Qiu0GY4E9Moj2v3FI45uy'
consumer = oauth.Consumer(consumer_key,consumer_secret)
token = oauth.Token(key=access_token_key, secret=access_token_secret)
client = oauth.Client(consumer, token)


def oauth_req(url, key, secret, http_method="GET", post_body=None,
 http_headers=None):
 resp, content = client.request(
 url,
 method=http_method,
 body="",
 headers=http_headers
 #force_auth_header=True
 )
 return content

if __name__ == '__main__':
    home_timeline = oauth_req(
    'https://api.twitter.com/1.1/search/tweets.json?q=%23freebandnames',
    'consumer_key',
    'consumer_secret' )
    #jdict = json.loads(home_timeline)
    print home_timeline
   



