#!/usr/bin/python

import sys

ip_counter = 0

for line in sys.stdin:
    ip = line.strip()
    if ip == "10.99.99.186":
		ip_counter = ip_counter + 1

print ip_counter
