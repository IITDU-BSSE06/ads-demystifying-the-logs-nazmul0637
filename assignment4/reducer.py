#!/usr/bin/python
import sys
dict = {}
for line in sys.stdin:
	file_path = line.strip()
	dict[file_path] = dict.get(file_path, 0) + 1
file_path_that_max_hitted = max(dict, key=dict.get)
print str(dict[file_path_that_max_hitted])
