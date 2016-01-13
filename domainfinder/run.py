'''
Created on Aug 29, 2015

@author: kim
'''

import pymongo
import time
import random

from domainmaker import makedomain
from domainchecker import checkDomain_checkDomain#, checkDomain_whois
#check = [checkDomain_checkDomain, checkDomain_whois]

#check = [checkDomain_checkDomain,]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "domainscraper"
MONGODB_COLLECTION_SCRAPED_DATA = "scrapeddata"
MONGODB_COLLECTION_CHECKED_DOMAINS = "domains"


client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)

db = client[MONGODB_DB]
collection_scraped = db[MONGODB_COLLECTION_SCRAPED_DATA]
collection_domains = db[MONGODB_COLLECTION_CHECKED_DOMAINS]


for doc in collection_scraped.find():
    
    domain = makedomain( doc["word"] )
    
    if collection_domains.find({'domain': domain}).count() > 0: continue
    
    exist=False
    #TODO: add sleep/wait, or rotate between diferent sources for domain name checking
    time.sleep(2)
    #random.shuffle(check)
    if not checkDomain_checkDomain(domain):
        print "taken:",domain
        continue
    print "________________________________________________________"
    print "FREE: ", domain
    print "________________________________________________________"       
    with open('domains.txt', 'w') as the_file:
        the_file.write(domain)
    
    
    
    


    

        
   
    