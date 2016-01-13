'''
Created on Aug 29, 2015

@author: kim
'''

import re

def makedomain(word,sufix="com"):
    """
    """
    domain=word
    domain = domain.lower()
    domain = re.sub(r'\W+', '', domain)
    
    return domain+"."+sufix


#s = "This isn`t my 555 domain"

#print makedomain(s)