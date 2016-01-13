'''
Created on 26. aug. 2015

@author: kga
'''
import urllib2
import re

def checkDomain_checkDomain(domain):
    site='http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=' + domain
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}
    req = urllib2.Request(site, headers=hdr)
    response = urllib2.urlopen(req)
    data = response.read()
    
    pat = re.compile("has already been registered by the organization below")
    pat2 = re.compile("he domain that you requested, <B>"+domain+"</B>, has already been registered.")
    
    patok = re.compile("The domain that you requested, <B>"+domain+"</B>, is still available!")
    
    #print data
    if pat.search(data) or pat2.search(data):
        return False
    elif patok:
        return True


"""from whois import whois   
def checkDomain_whois(domain):
    try:
        details = whois(domain)
        return False
    except Exception, e:
        if 'no match for "'+domain+'".' in str(e).lower():
            return True
    return False
"""


#print checkDomain_checkDomain("afictionaluniverse.com")