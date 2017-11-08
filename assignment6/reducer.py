#!/usr/bin/python
import sys
count_9=0
count_10=0
count_11=0
for line in sys.stdin:
	year = line.strip()
	if year == "2009":
		count_9 +=1 
	if year == "2010":
		count_10 +=1
	if year == "2011":
		count_11 +=1
		
print "2009 "+ str(count_9) + "\n" +  "2010 " + str(count_10) + "\n" + "2011 " + str(count_11) + "\n"
