#!/usr/bin/python
import sys
NumOfUniqueFiles = set()
for line in sys.stdin:
	file_path = line.strip()
	NumOfUniqueFiles.add(file_path)

print str(len(NumOfUniqueFiles))
