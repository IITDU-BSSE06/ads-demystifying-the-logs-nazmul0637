#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split(":")
	if len(data) > 1:
		new_data=data[0].strip().split("/")
		year = new_data[2]

		print year
