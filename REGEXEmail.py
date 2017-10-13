# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from collections import Counter

emailFilePath = 'C:/Users/Jeffrey/Documents/MSBA/REGEX/hillary-clinton-emails-august-31-release_djvu(1).txt'
email = open(emailFilePath,'r')
emailList = []
results = {}
for line in email.readlines():
        for thisMatch in re.finditer('[\w_.+-]+@[\w_.+-]+', line):
            if thisMatch:
#               print "   --indicates a match--    ", thisMatch.group(), thisMatch.start(), thisMatch.end(), thisMatch.span()
                emailList.append(thisMatch.group())
                
results = dict(Counter(emailList))

print "The top five most used email addresses are as follows:"
print
 
loop = 0
for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse = True):
    if loop < 6: 
        print "%s: %s" % (key, value)
        loop += 1
    else: 
        break

email.close()
#print 'numRecords:', len(results)