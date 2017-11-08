#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split('"')
	if len(data) > 1:
		new_data=data[1].strip().split(" ")
		http_request = new_data[0]

		print http_request
