#!/usr/bin/python

import sys

path_counter = 0

for line in sys.stdin:
    path = line.strip()
    if path == "/assets/js/the-associates.js":
		path_counter = path_counter + 1

print path_counter
