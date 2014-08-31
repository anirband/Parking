#!/usr/bin/python
import httplib2
import string
import random

def randomstring(size=15, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))  


#User agent in the HTTP request set to an old version of IE, and set the referrer to google search, just so it seemed to the website that the user is running an old browser and coming from a search engine

def parking(domain):
	h=httplib2.Http(".cache_httplib")
	h.follow_all_redirects=True
	try:
		random_subdomain=randomstring()
		if(domain[:7]!='http://'):
		    link='http://'+random_subdomain+'.'+domain+'/'
		resp,content=h.request(link,'GET',headers={'User-Agent':'Mozilla/4.0(compatible; MSTE 5.5; Windows 98; Win 9x 4.90)','Content-Type':'text/plain', 'Referer': 'http://www.google.com/search?hl=fr&q=dictionary+french'})
		contentLocation=resp['content-location'] 
		if(contentLocation!=''):
		    return('Positive')
	except:	    
	    return('Negative')



