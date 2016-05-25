#!/usr/bin/env python

import sys
import string

allsent={}
sent_num=0
start=0
char_count=0
totalchar = 0

for lines in sys.stdin:
  line = lines.strip()
  
  for char in line: 
    #checking the characters using ASCII values   
    if (ord(char)>=65)and (ord(char)<=90):
        char_count = 1
        start = 1

    #cheking the termination condition for a sentence
    elif (char=='.' or char=='?' or char=='!') and start==1:
        char_count = char_count + 1
        sent_num = sent_num + 1
        allsent[(sent_num)] = char_count
        totalchar = totalchar + char_count
        start = 0

    elif (char==char.lower()) and start==1:
        char_count = char_count + 1        

 
#allsent['char']=totalchar
#allsent['sentence']=sent_num 

     
print '%s\t%s' %('sentence',sent_num)
print '%s\t%s' %('char',totalchar)





