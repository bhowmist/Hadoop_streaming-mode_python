#!/usr/bin/env python

import sys
import string

tot_sentence=0.0
tot_char=0.0

for line in sys.stdin:
  (key,val) = line.split('\t',1)
   
  if key=='sentence':
      tot_sentence = tot_sentence + float(val)

  elif key=='char':
      tot_char = tot_char + float(val)

print "SentenceCount      ",int(tot_sentence)
print "AvgSentenceLength  ", (tot_char/tot_sentence)
                
         
	
	
