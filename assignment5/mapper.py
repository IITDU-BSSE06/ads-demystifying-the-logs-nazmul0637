#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split("GET")
	if len(data) > 1:
		file_path = urlparse(data[1].split()[0]).path
		if file_path:
			print str(file_path)
