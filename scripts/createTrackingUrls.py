#! /usr/bin/env python

##one time use to generate a bunch of tracking id's
# Katie Li
# 02/09/2014
import urllib2
import keys

#http://tiny.cc/?c=rest_api&m=shorten&version=2.0.3&format=json&longUrl=urlencode('http://example.com')&login=tinyccapidemo&apiKey=YourKey

sc_url="http://www.claremontenergy.org/"
shortUrl= 'Claremont_'
my_key = keys.key
login  = keys.login
base_url = 'http://tiny.cc/?c=rest_api&m=shorten&version=2.0.3&format=json&longUrl={0}&shortUrl={1}&login={2}&apiKey={3}'

for i in range(1, 20): 
    #concatenate the strings
    post_url = base_url.format(sc_url, shortUrl + str(i), login, my_key)
    print post_url
    response =urllib2.urlopen(post_url) 
    print response.read()
  
